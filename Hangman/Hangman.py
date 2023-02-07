#Project description: the program makes a word, and the user has to guess it.
# Initially, all letters of the word are unknown. A gallows with a noose is also drawn.
# The user suggests a letter that can be included in this word. If there is such a letter in the word,
# then the program puts the letter as many times as it occurs in the word.
# If there is no such letter, a circle in a loop representing a head is added to the gallows.
# The user continues to guess the letters until he guesses the whole word. For each unsuccessful attempt,
# another part of the hangman's torso is added (usually there are 6 of them: head, torso, 2 arms and 2 legs.
#
#Components of the project:
#
#Integers (int type);
#Variables;
#Data input/output (input() and print() functions);
#Conditional operator (if/elif/else);
#While loop;
#Infinite loop;
#Break, continue operators;
#Creating custom functions;
#List expressions;
#Working with the random module to generate random numbers.

import random
import re

words = """
absence , absorption , acceleration , acceptance , accessory , accident , active , address , adjacent , adventure , advice , age , agent , agency , ago , allowance , along , also , alternative , always , ambition , amplitude , anchor , ankle , appendage , application , approximation , arbitration , arbitrary , arc , area , arrangement , ash , asset , assistant , average , awkward , axis .

balcony , bale , bankrupt , bark , barrel , beak , beaker , beard , beat , behind , belt , bet , bill , birefringence , blame , blanket , both , bottom , brave , break, breakfast , breast , broker , bubble , bud , budget , buoyancy , bunch , burial , busy .

calculation , call , capacity , capital , carpet , cartilage , case , cast , cave , cavity , cell , ceremony , certificate , chair , character, charge , child , chimney , china , choice , circulation , circuit , circumference , civilization , clay , claim , claw , cleavage , clever , client , climber, clip , code , coil , collision , collection , column , combination , combine , communications , complaint , component , compound , concept , concrete , conductor , congruent , conservation , consignment , constant , consumer , continuous , contour , convenient , conversion , cool , corner , correlation , corrosion , cost , court , creeper , crop , cross , cunning , cusp , customs .

damping , date , debit , deck , decrease , defect , deficiency , deflation, degenerate , delivery , demand , denominator , department , desert , density , deposit , determining, dew , diameter , difference , difficulty , drift, dike , dilution, dinner , dip , direct, disappearance , discharge , discount , disgrace , dislike , dissipation , disturbance , ditch , dive , divisor , divorce , doll , domesticating , dreadful , dream , duct , dull , duty .

each , easy , economy , efficiency , effort , either , elimination , employer , empty , enemy , envelope , environment , envy , equation , erosion , eruption , evaporation , evening , exact , excitement , experiment, exercise , explanation , explosion , export , expression , extinction , eyebrow , eyelash .

factor , failure , fair , famous , fan , fastening , fatigue , fault, ferment , fertilizing , fever , fiber, figure , fin, financial , flash , flask , flesh , flood , flour , focus , forecast , forehead , foreign , forgiveness , fraction , fracture , fresh , friction, flint , flood , flow , foliation , frost , frozen , fume , funnel , funny , fur , furnace , furniture , fusion .

gate , generation , germ , germinating , gill , glacier , gland, god , grand , grateful , grating , gravel , grease , grief , grocery , groove , gross, ground , guard , guarantee, guess , gum .

habit , handkerchief , handle , heavy , hedge , hill , hinge, hire , hold , holiday , home , honest , honey , hoof , host , human , hunt , hurry , hurt , husband .

igneous , image , imagination , import , impurity , inclusion , index , individual , inflation , infinity , inheritance , innocent , institution , insulator , integer , intelligent , intercept , interpretation , intersection, intrusion , investigation , investment , inverse , invitation .

jam , jaw , jealous , jerk , joint , jug , juice , jury , justice .

kennel , kidney , kitchen , knock

lace , lag , lake , lamb , lamp , large , latitude, lawyer , layer , lazy , lecture , legal , length, lens , lesson , lever , liability , license , lid , life , lime , limestone , link , liver , load , local , load , loan, locus , loop , longitude , luck , lump , lunch , lung .

magic , magnitude, manner , many , marble , margin , marriage , mast , mattress , mature mean , meaning , medicine , medium , melt , member , mess , message , metabolism , mill , mineral , mixture , model , modern , modest , momentum , monopoly , mood , moral , moustache , mud , multiple , multiplication , murder .

nasty , nature , navy , neat , neglect , neighbor , nest , next , nice , node , nostril , nucleus , numerator, nurse .

obedient , oblique , officer , orchestra , ore , organ , origin , outcrop , outlier , overlap , oval , own , oxidation .

packing, pad , pair , pan , paragraph , parent , particle , partner , party , passage , path , patience , pedal , pendulum , pension , people , perfect , petal , piston , plain, plan , plaster , plug , poetry , pollen , pool , population , porcelain , practice , praise , prayer , pressure, prick , priest , prime , probability , product , progress , projectile , projection , promise , proof , proud , pulley , pupil , purchase , pure .

quantity , quotient.

race , radiation, ratio, reagent , real , receiver , reciprocal , rectangle , recurring , reference , reflux , reinforcement , relative , remark , remedy , rent , repair , reproduction , repulsion , resistance , residue , resolution , result , retail , revenge , reversible , rich , rigidity , rise, rival , rock , rot , rotation , rude , rust .

sac , sale , sample , satisfaction , saturated , saucer , saving , scale , scarp , schist , scratch , screen , seal , search , security , secretion , section , sedimentary , selfish , sensitivity , sentence , sepal , service , set , shadow , shale, share , shave , shear, sheet , shell , shore , shoulder , show , sight , sill , similarity , since , skull , slate , sleeve , slide , social , soil , soldier , solution , solvent , sorry , spark , specialization , specimen , speculation , spirit , spit , splash , spot , stable , stain , stair , stalk , stamen, statistics , steady , stimulus , storm , strain , straw , stream , strength , stress , strike , string , study , subject , substitution , subtraction , success , successive , sucker , sum , supply , surface , surgeon , suspension , suspicious , swelling , swing , switch , sympathetic .

tailor , tame , tap , tear , tent , term , texture , thickness , thief , thimble , thorax , threat , thrust , tide , tie , tissue , tongs , too , total , towel , tower , traffic , tragedy , transmission , transparent , trap , travel , treatment , triangle , truck , tube , tune , tunnel , twin , typist .

ugly , unconformity, understanding , universe , unknown .

valency , valley , valve , vapor , variable , vascular , vegetable , velocity , vestigial , victim , victory , volume , vortex , vote .

weak , wedge , welcome , whether , wholesale , widow , wife , wild , world , wreck , wrist .

yawn.
"""

message_lets_play = 'Давайте играть в угадайку слов!'
win_message = 'Поздравляем, вы угадали слово! Вы победили!'

yes_answers = ("yes", "y", "да")
no_answers = ("no", "n", "нет")

word_list = words.replace(",", "").replace(".", "").split()


def ask_bool_yes_no(message):
    while True:
        print(message + "(enter yes or no)")
        answer = input().lower()
        if answer in yes_answers:
            return True
        elif answer in no_answers:
            return False


def get_word():
    return random.choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    print(stages[tries])


def find_all(string, substring):
    return tuple(i.start() for i in re.finditer(substring, string))


def play(word):
    # тело функции
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print(message_lets_play)

    display_hangman(tries)
    print(word_completion)

    while True:
        print("Enter a letter or a word:")
        user_input = input().upper()
        if user_input.isalpha():
            if user_input in guessed_words:
                print("You have already entered this word")
                continue
            elif user_input in guessed_letters:
                print("You have already entered this letter")
                continue
            else:
                finded_indexes = find_all(string=word, substring=user_input)
                if len(user_input) >= 2:
                    guessed_words.append(user_input)
                else:
                    guessed_letters.append(user_input)

                if len(finded_indexes) < 1:
                    print("Not right.")
                    tries -= 1
                    display_hangman(tries)
                    if tries < 1:
                        print()
                        print("--- FAIL ---")
                        print()
                        print(f"Target word: {word}")
                        return

                for finded_index in finded_indexes:
                    word_completion = word_completion[:finded_index] + user_input + word_completion[
                                                                                    finded_index + len(user_input):]
                print(word_completion)

                if "_" not in word_completion:
                    guessed = True
                    print()
                    print(win_message)
                    print()
                    return
        else:
            print("You entered non-alphabetical sequence.")


def main():
    while True:
        generated_word = get_word()
        play(generated_word)
        play_again = ask_bool_yes_no("Should we play again?")
        if play_again:
            continue
        else:
            break


if __name__ == "__main__":
    main()