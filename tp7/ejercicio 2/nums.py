alphabet ="abcdefghijklmnñopqrstuvwxyz"


class Pin:
    def validate_pin(self, pin):
        if len(pin) == 4 or len(pin) == 6:
            for i in pin:
                if i.lower() in alphabet:
                    return False
            return True
        else:
            return False
