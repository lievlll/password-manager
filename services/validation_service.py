class ValidationService:

    @staticmethod
    def not_empty(value):
        return isinstance(value, str) and len(value.strip()) > 0
