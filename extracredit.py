def is_valid_part(part):
    try:
        i_part = int(part)
        if part [0] == '0' and not i_part == 0: return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
    return True

def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return decimal_to_binary(next) + str(digit)

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP Address"
    parts = ip.split('.')
    binary_octets = []

    for part in parts:
        n = int(part)
        if n == 0:
            res = "0"
        else:
            res = decimal_to_binary(n)
        padded_res = res.zfill(8)
        binary_octets.append(padded_res)
    return ".".join(binary_octets)

print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"