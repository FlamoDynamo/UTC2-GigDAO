from algosdk.v2client import algod
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from smart_contracts.contract.contract import GigDAOContract
from algosdk.mnemonic import to_private_key

def deploy():
    # Sử dụng Algonode.io cho testnet
    algod_address = "https://testnet-api.algonode.cloud"
    algod_token = ""  # Algonode không yêu cầu token
    
    try:
        # Khởi tạo Algod client
        algod_client = algod.AlgodClient(algod_token, algod_address)

        # Kiểm tra kết nối
        status = algod_client.status()
        print(f"Kết nối thành công. Phiên bản node: {status['last-round']}")

        # Lưu ý: Bạn cần cung cấp địa chỉ và mnemonic của người triển khai
        address = "MV7HWZVFW64CK2A5JCUEXXWORNZRIRQLPPNAUPO4IP4AHMZ7XB6BU2ZSNM"
        mnemonic_phrase = "tree river prefer carry lift together charge priority cloud oxygen model twin hockey citizen deputy baby flip security bullet dry seat concert special about pride"

        # Chuyển mnemonic thành private key
        private_key = to_private_key(mnemonic_phrase)

        print(f"Địa chỉ người triển khai: {address}")

        # Tạo khóa AES (hoặc sử dụng khóa có sẵn)
        aes_key = "bzT4VCCw0HEF3FIiTZfH32VHnWYCBJdJfWXj1AHfkug="  # Khóa AES đã được tạo sẵn

        # Triển khai GigDAO Contract với aes_key
        gig_dao_contract = GigDAOContract(algod_client, aes_key)

        # Truyền thêm tham số name và description
        dao_name = "GigDAO"
        dao_description = "DAO for managing decentralized gig projects"
        gig_dao_app_id = gig_dao_contract.create_dao(address, private_key, dao_name, dao_description)

        print(f"GigDAO Contract đã được triển khai với app_id: {gig_dao_app_id}")

        print("Tất cả các contract đã được triển khai thành công!")

    except Exception as e:
        print(f"Lỗi khi triển khai: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    deploy()