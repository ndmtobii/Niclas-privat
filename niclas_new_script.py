# 1. How many valid participants have been collected each day and in total?

import json


# Stores data from collection_log.json
collection_log_list = []
# Stores all valid participants.
valid_participant_list = []
# Stores data from participants.json
list_of_participants = []

    # Opens the collection log to get all the participants.
with open('collection_log.json', 'r') as collected:
    collected_participants = json.load(collected)
    for i in range(len(collected_participants["Participants"])):
        # Inserts ID to index 0 of collection_log_list.
        id_coll = collected_participants["Participants"][i]["ID"]
        collection_log_list.insert(0, id_coll)
        # Inserts Date to index 1 of collection_log_list.
        date_coll = collected_participants["Participants"][i]["Date"]
        collection_log_list.insert(1, date_coll)
        # Inserts sequence to index 2 of collection_log_list.
        seq_coll = collected_participants["Participants"][i]["Collection sequence"]
        collection_log_list.insert(2, seq_coll)
        # print("ID :", collection_log_list[0], "Date:", collection_log_list[1], "Sequence: ", collection_log_list[2])

        # Making easy to access variables for ID, Date, Sequence and one variable to access them all as "collected_test_index"
        id_coll_index = collection_log_list[0]
        date_test_index = collection_log_list[1]
        seq_test_index = collection_log_list[2]
        collected_test_index = id_coll_index, date_test_index, seq_test_index
        # print(collected_test_index)

# I need to make sure the participants are valid by comparing them with participants.json.
with open('participants.json', 'r') as participant_list:
    available_participants = json.load(participant_list)
    for i in range(len(available_participants["Participants"])):
        # Inserts ID to index 0 of list_of_participants.
        id_list = available_participants["Participants"][i]["ID"]
        list_of_participants.insert(0, id_list)
        # Inserts Group to index 1 of list_of_participants.
        group_list = available_participants["Participants"][i]["Group"]
        list_of_participants.insert(1, group_list)
        # Inserts Age to index 2 of list_of_participants.
        age_list = available_participants["Participants"][i]["Age"]
        list_of_participants.insert(2, age_list)
        # Inserts Gender to index 3 of list_of_participants.
        gender_list = available_participants["Participants"][i]["Gender"]
        list_of_participants.insert(3, gender_list)


        # Making easy to access variables for ID, Group, Age, Gender and one variable to access them all as "available_index"
        id_list_index = list_of_participants[0]
        group_list_index = list_of_participants[1]
        age_list_index = list_of_participants[2]
        gender_list_index = list_of_participants[3]
        available_index = id_list_index, group_list_index, age_list_index, gender_list_index
        # Removes invalid participants from list_of_participants
        if group_list_index == 'C' and age_list_index <= 60:
            list_of_participants.remove(id_list)
            # print(available_index)





















def main():



    if __name__ == "__main__":
        main()
