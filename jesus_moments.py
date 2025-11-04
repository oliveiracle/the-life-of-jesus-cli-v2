# ==============================================================================
# THE LIFE OF JESUS CHRIST - MOMENTS MODULE
# ==============================================================================
# This module contains formatted titles for the 25 key moments
# in the life of Jesus Christ, with enhanced ASCII art using art library
# ==============================================================================

from art import text2art
from colorama import Fore, init
init(autoreset=True)


def show_title():
    """Display the main title of the application with fancy ASCII art"""
    # Generate fancy ASCII art for "JESUS"
    title_art = text2art("JESUS CHRIST", font='standard')

    print(Fore.CYAN + title_art)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.CYAN + "         THE LIFE OF JESUS CHRIST CLI".center(60))
    print(Fore.YELLOW + "=" * 70)
    print()
    print(Fore.YELLOW + "🙏 'For God so loved the world that He gave "
          "His one and only Son,")
    print("   that whoever believes in Him shall not perish")
    print("   but have eternal life'")
    print(Fore.WHITE + "📖 John 3:16")
    print(Fore.YELLOW + "=" * 70)
    print()


# ==============================================================================
# MOMENT TITLES - Formatted strings for each moment
# ==============================================================================

# BIRTH & CHILDHOOD (1-3)
moment1 = "the angel gabriel announces jesus' birth to mary"
moment1_formatted = moment1.title()

moment2 = "the birth of jesus christ in bethlehem"
moment2_formatted = moment2.title()

moment3 = "young jesus at the temple"
moment3_formatted = moment3.title()


# BEGINNING OF MINISTRY (4-7)
moment4 = "the baptism of jesus by john"
moment4_formatted = moment4.title()

moment5 = "jesus' temptation in the wilderness"
moment5_formatted = moment5.title()

moment6 = "calling the first disciples"
moment6_formatted = moment6.title()

moment7 = "first miracle - water into wine at cana"
moment7_formatted = moment7.title()


# POWERFUL MIRACLES (8-13)
moment8 = "healing the paralytic man"
moment8_formatted = moment8.title()

moment9 = "calming the storm on the sea"
moment9_formatted = moment9.title()

moment10 = "feeding the five thousand"
moment10_formatted = moment10.title()

moment11 = "walking on water"
moment11_formatted = moment11.title()

moment12 = "raising lazarus from the dead"
moment12_formatted = moment12.title()

moment13 = "healing the blind man"
moment13_formatted = moment13.title()


# PROFOUND TEACHINGS (14-17)
moment14 = "the sermon on the mount"
moment14_formatted = moment14.title()

moment15 = "the parable of the prodigal son"
moment15_formatted = moment15.title()

moment16 = "jesus declares: i am the way, the truth, and the life"
moment16_formatted = moment16.title()

moment17 = "the greatest commandment: love god and love others"
moment17_formatted = moment17.title()


# FINAL WEEK (18-25)
moment18 = "triumphal entry into jerusalem"
moment18_formatted = moment18.title()

moment19 = "the last supper with the disciples"
moment19_formatted = moment19.title()

moment20 = "prayer in the garden of gethsemane"
moment20_formatted = moment20.title()

moment21 = "the trial and condemnation of jesus"
moment21_formatted = moment21.title()

moment22 = "the crucifixion at calvary"
moment22_formatted = moment22.title()

moment23 = "it is finished - jesus' final words"
moment23_formatted = moment23.title()

moment24 = "the resurrection - he is risen!"
moment24_formatted = moment24.title()

moment25 = "the ascension into heaven"
moment25_formatted = moment25.title()
