class Task:
    def __init__(self):
        self.__done: bool = False
        self.__label: str = ""
        self.__created_at: float = 0
        self.__updated_at: float = 0

    # Getters
    def get_done(self):
        return self.__done
    
    def get_label(self):
        return self.__label;

    def get_created_at(self):
        return self.__created_at

    def get_updated_at(self):
        return self.__updated_at

    # Setters
    def done(self, done: bool):
        self.__done = done
        return self
    
    def label(self, label: str):
        self.__label = label
        return self

    def created_at(self, created_at: float):
        self.__created_at = created_at
        return self

    def updated_at(self, updated_at: float):
        self.__updated_at = updated_at
        return self

    def to_json_format(self):
        return {
            "done": self.__done,
            "label": self.__label,
            "createdAt": self.__created_at,
            "updatedAt": self.__updated_at
        }
