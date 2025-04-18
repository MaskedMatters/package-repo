import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="Version Tester",
        description="A simple CLI tool for testing version updates and phrases. This tool doesn't do much yet, but it's great for testing CLI structure!",
        epilog="Version Tester v0.0.1 - More features coming soon. Stay tuned!"
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='Version Tester v0.0.1'
    )

    parser.add_argument(
        'command',
        nargs='?',
        help='Type "phrase" to see a cool phrase!'
    )

    args = parser.parse_args()

    if args.command is None:
        return

    if args.command == "phrase":
        print("🚀 Keep calm and test your versions!")
        return

    if args.command:
        print("How's it going?")

if __name__ == '__main__':
    main()
