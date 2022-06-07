#!/usr/bin/python3
"""
Task 1 :
private class attr, constructor, validate
"""
import json
import os
import csv


class Base:
    """
    Clase base
    I need access to my class to modify private clas
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """"initialize"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """transform object py to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of objs(json string) in afile with variable name"""
        list_algo = []
        name_of_file = f"{cls.__name__}.json"

        if list_objs is not None and len(list_objs) != 0:
            for algo in list_objs:
                list_algo += [algo.to_dictionary()]

        json_list = Base.to_json_string(list_algo)

        with open(name_of_file, "w", encoding="UTF-8") as f:
            f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """convert json string to object python"""
        if json_string is not None and len(json_string) != 0:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """create a new instance of Square or Rectangle"""
        instance_dady = cls.__name__

        if instance_dady == "Square":
            dummy = cls(2)

        if instance_dady == "Rectangle":
            dummy = cls(2, 2)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """list of instances in a file"""
        ins_list = []
        name_of_file = f"{cls.__name__}.json"

        if os.path.exists(name_of_file) is False:
            return ins_list

        with open(name_of_file, mode="r", encoding="utf-8") as f:
            dicts = cls.from_json_string(f.read())

            for data in dicts:
                ins_list.append(cls.create(**data))

            return ins_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save csv attr in format csv into file
        (if exitsts)
        """
        inst_name = cls.__name__
        name_of_file = inst_name + ".csv"

        if inst_name == "Rectangle":
            if list_objs is not None:
                with open(name_of_file, mode="w", newline='') as f:
                    w = csv.writer(f)
                    for i in list_objs:
                        w.writerow([i.id, i.width, i.height, i.x, i.y])

        if inst_name == "Square":
            if list_objs is not None:
                with open(name_of_file, mode="w", newline='') as f:
                    l_writer = csv.writer(f)
                    for inst in list_objs:
                        l_writer.writerow([inst.id, inst.size, inst.x, inst.y])

    @classmethod
    def load_from_file_csv(cls):
        """create a list of instances from a file with csv format"""
        inst_name = cls.__name__
        name_of_file = inst_name + ".csv"
        res_list = []

        with open(name_of_file, mode="r") as f:
            file_read = csv.reader(f)
            for ins in file_read:
                if inst_name == 'Rectangle':
                    dict = {"id": int(ins[0]), "width": int(ins[1]),
                            "height": int(ins[2]), "x": int(ins[3]),
                            "y": int(ins[4])}
                if inst_name == 'Square':
                    dict = {"id": int(ins[0]), "size": int(ins[1]),
                            "x": int(ins[2]), "y": int(ins[3])}
                res_list.append(cls.create(**dict))

        return res_list
