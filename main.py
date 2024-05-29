import words
import hangman
from random import choice

def get_random_word():
  return choice(words.easy_wordlist)

def draw_hangman(attempt):
  return hangman.hangman_parts[attempt]
  

def main():
  choosen_word = get_random_word()
  enumerate_choosen_word = enumerate(choosen_word)
  print('Welcome to hangman!')
  print(f'The word has {len(choosen_word)} letters.')
  print('You have 7 tries to guess the word.')

  attempts = 7
  guessed_letter = set()
  display_word = ['_'] * len(choosen_word)

  while attempts > 0 or '_' in display_word:
    print(draw_hangman(attempts))
    print(''.join(display_word))
    
    guess = input('Guess a letter or the word: ').lower()

    #if pertama untuk mengatasi input yang salah dan kedua dan ketiga untuk mengatasi tebakan
    #yang salah
    if not guess.isalpha() or not guess:
      print('That is not a letter')
      continue
    elif len(guess) == len(choosen_word) and guess != choosen_word:
      attempts -= 1
      print(f"Wrong guess! You have {attempts} attempts left.")
      continue
    elif guess in guessed_letter:
      print("You already guessed that letter.")
      continue

    guessed_letter.add(guess)

    #game mechanic
    if guess in choosen_word:
      for pos, letter in enumerate_choosen_word:
        if letter == guess:
          display_word[pos] = letter
    else:
      attempts -= 1
      print(f"Wrong guess! You have {attempts} attempts left.")

    if guess == choosen_word:
      print(f"Congratulations! You guessed the word: {choosen_word}")
      break
    elif '_' not in choosen_word:
      print(f"Congratulations! You guessed the word: {choosen_word}")
      break
    else:
      print(draw_hangman(attempts))
      print(f"Game over! The word was: {choosen_word}")
      break
        

if __name__ == "__main__":
  main()

#MASIH SALAH. PERBAIKI
