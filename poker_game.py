#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:47:27 2019

@author: anikarawat
"""

import sys
import copy
from random import shuffle

first_input = int(sys.argv[1]) 
print(first_input)
card_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def start(num_of_players): 
    names = []
    for i in range(num_of_players): 
        new_name = input("What is the name of player?")
        names.append(new_name)
    #print(names)
    new_deck = create_deck()
    #print(new_deck)
    #shuffle method here shuffles in place and does not return anything
    shuffle_three_times(new_deck)
    #print(new_deck)
    hands = deal_cards(new_deck, num_of_players)
    original_hands = copy.deepcopy(hands)
    winning_hand = compare_hands(hands)
    declare_winner(winning_hand, names, original_hands)
  
def create_deck(): 
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    return deck

def shuffle_three_times(deck): 
    for i in range(3): 
        shuffle(deck)

def deal_cards(deck, player_num):       
    #create deck and one hand 
    hands = []
    card = 1;
    #print(player_num)
    for i in range(player_num): 
            new_hand = []
            hands.append(new_hand)
    while card <= 5: 
        for hand in hands: 
            hand.append(deck.pop())
        card += 1
        #print(hands)
        #print(deck)
    #returns a list of hand lists
    print(hands)
    return hands

def compare_hands(hands):
    #create a list of lists with all values and no letters and SORTED
    for hand in hands: 
        for i in range(len(hand)): 
            if type(hand[i]) != int: 
                hand[i] = card_values.get(hand[i])
        hand = hand.sort(reverse = True) 
    print(hands)
        
    max_values = find_max_values(hands)
    #some loop to make sure unique vals 
    while any(max_values.count(max(max_values)) > 1 for i in max_values) == True:
        max_values = find_max_values(hands)
    win_hand_value = max(max_values)
    #if win_hand_value > 10: 
        #for card, val in card_values.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
            #if val == win_hand_value:
                #win_hand_value = card
    return max_values.index(win_hand_value)
    
def find_max_values(hands):
    max_list = []
    for i in range(len(hands)): 
        max_list.append(hands[i][0])
        hands[i].remove(hands[i][0])
    print(max_list)
    return max_list
        
def declare_winner(winIndex, names, orig_hands): 
    print("Winner is player ", names[winIndex])
    print("Winning card hand is: ", orig_hands[winIndex])
    
    
start(first_input)
