import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Publish messages to a RabbitMQ queue.")
    
    parser.add_argument(
        "-c", "--channel",
        type=str,
        help="Channel name (queue name)",
        required=True
    )
    
    parser.add_argument(
        "-cc", "--country_code",
        type=str,
        help="Country code",
        required=True
    )

    try:
        args = parser.parse_args()
        args.channel = args.channel.lower()
        args.country_code = args.country_code.lower()
        return args
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    args = parse_args()
    print(f"Channel: {args.channel}")
    print(f"Country Code: {args.country_code}")
