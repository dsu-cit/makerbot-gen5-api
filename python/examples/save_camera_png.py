#!/usr/bin/python
import makerbotapi
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "args: <output filename> <ip address of your gen5> [<AUTH CODE>]"
        sys.exit(1)
    output_filename = sys.argv[1]
    ip_address = sys.argv[2]

    if len(sys.argv) > 3:
        AUTH_CODE = sys.argv[3]
    else:
        AUTH_CODE = None

    makerbot = makerbotapi.Makerbot(ip_address, auth_code=AUTH_CODE)
    if AUTH_CODE == None:
        print "Press the flashing action button on your makerbot now"
        makerbot.authenticate_fcgi()
        print "Authenticated with code", makerbot.auth_code

    makerbot.authenticate_json_rpc()

    makerbot.save_camera_png(output_filename)
    print "Camera PNG saved to", output_filename
