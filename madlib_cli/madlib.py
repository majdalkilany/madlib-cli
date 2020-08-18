def welcom() :
    print('''welcom in madlib game
    
     please  fill the blanks in the words
    ''')

def write_file_befor_merge() :
    with open('mad_file.txt','w') as fname :
        fname.write('''

Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.                ''')


def read_file() :
    with open('mad_file.txt',) as fname :
        fname = fname.read()
        second_pos = 0
        counter_parn = fname.count('{')
        user_inputs = []
        for i in range(counter_parn):
            first_pos = fname.find('{',second_pos) + 1
            second_pos = fname.find('}',first_pos)
            # print(fname[first_pos:second_pos])
            the_word = fname[first_pos:second_pos]

            
            
            user_input = input(f' please  enter {the_word}  >> ')
            user_inputs.append(user_input)
            # print(user_inputs)

    return user_inputs , fname


def merge_and_write_file(user_inputs) :
        with open('mad_file.txt',) as fname :
            fname = fname.read()

        for i in range(len(user_inputs)) :
                first_pos = fname.find('{',0) 
                second_pos = fname.find('}',0)+1
                # print(fname[first_pos:second_pos])
                fname = fname[:first_pos] +user_inputs[i] + fname[second_pos:]
        # print(fname)

        with open ('Written_madlib.txt','w') as mad_lib_game :
            mad_lib_game.write(fname)
            return fname 

    


if __name__ == "__main__":
    user_inputs,file_name = read_file()
    merge_and_write_file(user_inputs)
# print(file_name)
