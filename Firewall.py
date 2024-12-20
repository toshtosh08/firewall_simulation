import random
from ipaddress import ip_address


def generate_random_ip():
    return f"192.168.1.{random.randint(0, 21)}"


def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"


def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.2": "block",
        "192.168.1.4": "block",
        "192.168.1.20": "block",
    }

    # Changed '*' to 'i' for proper loop syntax
    for i in range(12):
        ip_addr = generate_random_ip()  # Changed variable name to avoid confusion
        action = check_firewall_rules(ip_addr, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_addr}, Action: {action}, Random: {random_number}")


if __name__ == "__main__":  # Fixed the syntax for main check
    main()