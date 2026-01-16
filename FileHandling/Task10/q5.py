import pickle as pkl

strings='''Jai and Veeru are small-time crooks who are released from prison, where they are recruited by a former Inspector Thakur Baldev Singh to capture a notorious dacoit named Gabbar Singh wanted for ₹50,000,[a] as the duo had saved Thakur from a train robbery which makes Thakur to recruit them for the mission with an additional ₹20,000 reward. The duo leave for Thakur's village in Ramgarh, where Gabbar is residing and terrorising the villagers.

After reaching Ramgarh, Veeru falls for Basanti, a feisty, talkative horse-cart driver. Jai meets Thakur's widowed daughter-in-law Radha and falls for her, who later reciprocates his feelings. The two thwart Gabbar's dacoits, who came to extort money. During the festival of Holi, Gabbar's gang attacks the villagers where they corner Jai and Veeru, but the duo manage to attack and chase them away from the village. The duo are upset at Thakur's inaction (when Jai and Veeru were cornered, Thakur had a gun within his reach, but did not help them) and consider calling off the mission. Thakur reveals that a few years ago, Gabbar had killed his family (save for Radha and Ramlal), and had both his arms cut off; he concealed the dismemberment by always wearing a shawl, the sole reason he could not use the gun'''

word_list=['thakur','gabbar','veeru']

word_count_dict=dict()
for word in strings.lower().split(' '):
    try:
        word_count_dict[word]+=1
    except:
        word_count_dict[word]=1

# print(word_count_dict)
pkl.dump(word_count_dict,open('word_count_dict.pkl','wb'))

word_count=pkl.load(open('word_count_dict.pkl','rb'))
for s in word_list:
    print(s,word_count[s])