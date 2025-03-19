from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def main():
    configure()

    master_token = os.getenv('master_token')


if __name__ == "__main__":
    main()