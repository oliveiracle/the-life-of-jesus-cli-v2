import jesus_moments
from colorama import Fore, init
import random

init(autoreset=True)

# Encouraging verses for exit message
encouraging_verses = [
    ("Matthew 28:20",
     "I am with you always, to the very end of the age"),
    ("John 14:27",
     "Peace I leave with you; my peace I give you"),
    ("Philippians 4:13",
     "I can do all things through Christ who strengthens me"),
    ("Joshua 1:9",
     "Be strong and courageous. Do not be afraid"),
    ("Psalm 23:1",
     "The Lord is my shepherd, I lack nothing"),
    ("Romans 8:28",
     "All things work together for good to those who love God"),
    ("Jeremiah 29:11",
     "For I know the plans I have for you, declares the Lord"),
    ("Proverbs 3:5-6",
     "Trust in the Lord with all your heart"),
    ("Isaiah 41:10",
     "Do not fear, for I am with you"),
    ("2 Corinthians 12:9",
     "My grace is sufficient for you")
]

# Dictionary with all 25 moments titles for search
moments_data = {
    1: {
        'title': "Angel's Announcement",
        'location': "Nazareth, Mary's home",
        'people': ['Angel Gabriel', 'Mary'],
        'scripture': 'Luke 1:30-31'
    },
    2: {
        'title': "Birth in Bethlehem",
        'location': 'Bethlehem, in a manger',
        'people': [
            'Mary',
            'Joseph',
            'baby Jesus',
            'shepherds',
            'angels'
        ],
        'scripture': 'Luke 2:10-11'
    },
    3: {
        'title': "Jesus at Temple - Young Jesus teaches at 12 years",
        'location': 'Jerusalem Temple',
        'people': [
            'Jesus (age 12)',
            'Mary',
            'Joseph',
            'teachers of the law'
        ],
        'scripture': 'Luke 2:46-47'
    },
    4: {
        'title': "Baptism - Jesus is baptized by John",
        'location': 'Jordan River',
        'people': ['Jesus', 'John the Baptist'],
        'scripture': 'Matthew 3:16'
    },
    5: {
        'title': "Temptation - Jesus resists devil in wilderness",
        'location': 'Wilderness',
        'people': ['Jesus', 'the devil'],
        'scripture': 'Matthew 4:1'
    },
    6: {
        'title': "First Disciples - Jesus calls his followers",
        'location': 'Near Jordan River',
        'people': [
            'Jesus',
            'John the Baptist',
            'Andrew',
            'Simon Peter',
            'Philip',
            'Nathanael'
        ],
        'scripture': 'John 1:35-36'
    },
    7: {
        'title': "First Miracle - Water into wine at Cana",
        'location': 'Cana',
        'people': ['Jesus', 'Mary', 'servants'],
        'scripture': 'John 2:7-8'
    },
    8: {
        'title': "Healing Paralytic - Jesus heals and forgives sins",
        'location': 'Capernaum',
        'people': [
            'Jesus',
            'paralyzed man',
            'friends',
            'scribes',
            'Pharisees'
        ],
        'scripture': 'Luke 5:18'
    },
    9: {
        'title': "Calming Storm - Jesus commands wind and waves",
        'location': 'Sea of Galilee',
        'people': ['Jesus', 'disciples'],
        'scripture': 'Matthew 8:23-24'
    },
    10: {
        'title': "Feeding 5000 - Miracle of bread and fish",
        'location': 'Near Sea of Galilee',
        'people': ['Jesus', 'disciples', 'crowd of 5000 men'],
        'scripture': 'Matthew 14:19'
    },
    11: {
        'title': "Walking on Water - Jesus walks on the sea",
        'location': 'Sea of Galilee',
        'people': ['Jesus', 'disciples (including Peter)'],
        'scripture': 'Matthew 14:25-26'
    },
    12: {
        'title': "Raising Lazarus - Jesus brings Lazarus to life",
        'location': 'Bethany',
        'people': ['Jesus', 'Lazarus', 'Mary', 'Martha'],
        'scripture': 'John 11:43-44'
    },
    13: {
        'title': "Healing Blind - Jesus restores sight",
        'location': 'Jerusalem',
        'people': ['Jesus', 'blind man', 'Pharisees'],
        'scripture': 'John 9:25'
    },
    14: {
        'title': "Sermon on Mount - Jesus teaches Beatitudes",
        'location': 'Mountainside near Sea of Galilee',
        'people': ['Jesus', 'disciples', 'crowds'],
        'scripture': 'Matthew 5:1-2'
    },
    15: {
        'title': "Prodigal Son - Parable of God's forgiveness",
        'location': 'Not specified',
        'people': [
            'Jesus (teaching)',
            'father',
            'prodigal son',
            'older brother'
        ],
        'scripture': 'Luke 15:20'
    },
    16: {
        'title': "I Am the Way - Jesus declares divine nature",
        'location': 'Upper room in Jerusalem',
        'people': ['Jesus', 'disciples'],
        'scripture': 'John 14:6'
    },
    17: {
        'title': "Greatest Commandment - Love God and others",
        'location': 'Jerusalem (Temple)',
        'people': ['Jesus', 'Pharisees'],
        'scripture': 'Matthew 22:37-38'
    },
    18: {
        'title': "Triumphal Entry - Jesus enters Jerusalem",
        'location': 'Jerusalem',
        'people': ['Jesus', 'crowds', 'disciples'],
        'scripture': 'John 12:12-13'
    },
    19: {
        'title': "Last Supper - Jesus shares final meal",
        'location': 'Upper room in Jerusalem',
        'people': ['Jesus', 'disciples (including Judas)'],
        'scripture': 'Matthew 26:26'
    },
    20: {
        'title': "Gethsemane - Jesus prays before arrest",
        'location': 'Garden of Gethsemane',
        'people': ['Jesus', 'disciples (Peter, James, John)'],
        'scripture': 'Matthew 26:36'
    },
    21: {
        'title': "Trial - Jesus stands before Pilate",
        'location': 'Jerusalem (Sanhedrin, Pilate, Herod)',
        'people': [
            'Jesus',
            'Pilate',
            'Caiaphas',
            'Herod Antipas',
            'Sanhedrin'
        ],
        'scripture': 'Matthew 27:1-2'
    },
    22: {
        'title': "Crucifixion - Jesus dies on the cross",
        'location': 'Golgotha (near Jerusalem)',
        'people': ['Jesus', 'soldiers', 'criminals', 'crowds'],
        'scripture': 'Matthew 27:33, 38'
    },
    23: {
        'title': "It Is Finished - Jesus' final words",
        'location': 'Golgotha (cross)',
        'people': ['Jesus', 'soldiers'],
        'scripture': 'John 19:30'
    },
    24: {
        'title': "Resurrection - Jesus rises from the dead",
        'location': 'Tomb near Jerusalem',
        'people': [
            'Jesus',
            'Mary Magdalene',
            'disciples',
            'angels'
        ],
        'scripture': 'Matthew 28:5-6'
    },
    25: {
        'title': "Ascension - Jesus returns to heaven",
        'location': 'Near Bethany',
        'people': ['Jesus', 'disciples'],
        'scripture': 'Luke 24:51'
    }
}

# Display title
jesus_moments.show_title()

# Main loop
while True:
    # Main menu
    print("\n" + "=" * 70)
    print(Fore.CYAN + "\n✝\n  MAIN MENU - THE LIFE OF JESUS".center(60))
    print("=" * 70)
    print("\n📖 What would you like to explore?\n")
    print("1 - The 25 Key Moments of Jesus' Life")
    print("2 - The Parables of Jesus (5 important teachings)")
    print("3 - Search moments by keyword")
    print("\nType 'quit' to exit\n")
    print("=" * 70)

    main_choice = input(
        "\nYour choice (1, 2, 3, or 'quit'): "
    ).strip()

    # Quit with random encouraging verse
    if main_choice.lower() in ["quit", "q"]:
        verse = random.choice(encouraging_verses)
        print(Fore.CYAN + "\n✝ Thank you for exploring the life of "
              "Jesus!")
        print(Fore.YELLOW + f"\n🙏 '{verse[1]}'")
        print(Fore.YELLOW + f"   - {verse[0]}")
        break

    # Option 1: The 25 moments
    if main_choice == "1":
        while True:
            print("\n" + "=" * 70)
            print("Explore 25 key moments from the life of Jesus:")
            print("=" * 70)

            print("\n👶 BIRTH & CHILDHOOD:")
            print("1-Angel's Announcement | 2-Birth in Bethlehem | "
                  "3-Jesus at Temple\n")

            print("\n⚡ BEGINNING OF MINISTRY:")
            print("4-Baptism | 5-Temptation | 6-First Disciples | "
                  "7-First Miracle\n")

            print("\n🔥 POWERFUL MIRACLES:")
            print("8-Healing Paralytic | 9-Calming Storm | "
                  "10-Feeding 5000")
            print("11-Walking on Water | 12-Raising Lazarus | "
                  "13-Healing Blind\n")

            print("\n📖 PROFOUND TEACHINGS:")
            print("14-Sermon on Mount | 15-Prodigal Son")
            print("16-I Am the Way | 17-Greatest Commandment\n")

            print("\n✝ FINAL WEEK:")
            print("18-Triumphal Entry | 19-Last Supper | "
                  "20-Gethsemane")
            print("21-Trial | 22-Crucifixion | 23-It Is Finished")
            print("24-Resurrection | 25-Ascension\n")
            print("=" * 70)

            user_input = input(
                "\nEnter your choice (1-25), 'back' for main "
                "menu, or 'quit': "
            )
            option = user_input.strip()

            # Quit
            if option.lower() in ["quit", "q"]:
                verse = random.choice(encouraging_verses)
                print(Fore.CYAN + "\n✝ Thank you for exploring!")
                print(Fore.YELLOW + f"\n🙏 '{verse[1]}'")
                print(Fore.YELLOW + f"   - {verse[0]}")
                exit()

            # Back to main menu
            if option.lower() in ["back", "b"]:
                break

            # Try/except validation
            try:
                option_num = int(option)
                if option_num < 1 or option_num > 25:
                    print(Fore.RED + f"\n❌ '{option}' is not a "
                          "valid moment!")
                    print("\n💡 Please choose between 1 and 25.")
                    continue
            except ValueError:
                print(Fore.RED + f"\n❌ '{option}' is not a number!")
                print("\n💡 Enter a NUMBER between 1-25, 'back', "
                      "or 'quit'.")
                continue

            # Moment 1
            if option == "1":
                print("=" * 70)
                print(f"\n✨ Divine Announcement: "
                      f"{jesus_moments.moment1_formatted}")
                print("=" * 70)
                print("\n📍 Location: Nazareth, Mary's home")
                print("\n👥 Key People: Angel Gabriel and Mary")
                print("\n📅 Time: Approximately 6 BC")
                print()
                print("\n📖 KEY VERSE: Luke 1:30-31")
                print('\n💬 "Do not be afraid, Mary; you have found '
                      'favor with God. '
                      'You will conceive and give birth to a son, '
                      'and you are '
                      'to call him Jesus."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   This moment marked the beginning of God's "
                      "plan for salvation.")
                print("   God chose a humble young woman to bear the "
                      "Savior of the world.")
                print()
                print("\n💡 MARY'S FAITHFUL RESPONSE:")
                print('   "I am the Lord\'s servant. May your word '
                      'to me be fulfilled." - Luke 1:38')
                print()
                print("\n🙏 May we respond to God's call with the "
                      "same faith and humility!")
                input("\nPress Enter to continue...")

            # Moment 2
            elif option == "2":
                print("=" * 70)
                print(f"\n⭐ The Incarnation: "
                      f"{jesus_moments.moment2_formatted}")
                print("=" * 70)
                print("\n📍 Location: Bethlehem, in a manger")
                print("\n👥 Key People: Mary, Joseph, baby Jesus, "
                      "shepherds, angels")
                print("\n📅 Time: Approximately 4-6 BC")
                print()
                print("\n📖 KEY VERSE: Luke 2:10-11")
                print('\n💬 "Do not be afraid. I bring you good news '
                      'that will '
                      'cause great joy for all the people. Today in '
                      'the town '
                      'of David a Savior has been born to you; he is '
                      'the '
                      'Messiah, the Lord."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   God became flesh and dwelt among us!")
                print("   The eternal God took on human form to save "
                      "humanity.")
                print()
                print("\n🎵 THE ANGELS' SONG:")
                print('   "Glory to God in the highest heaven, and '
                      'on earth peace to those on whom his favor '
                      'rests!" - Luke 2:14')
                print()
                print("\n💡 John 1:14 - 'The Word became flesh and "
                      "made his dwelling among us.'")
                print()
                print("\n🙏 Jesus left heaven's glory to be born in "
                      "humility - for you and me!")
                input("\nPress Enter to continue...")

            # Moment 3
            elif option == "3":
                print("=" * 70)
                print(f"\n📚 Early Wisdom: "
                      f"{jesus_moments.moment3_formatted}")
                print("=" * 70)
                print("\n📍 Location: Jerusalem Temple")
                print("\n👥 Key People: Jesus (age 12), Mary, "
                      "Joseph, teachers")
                print("\n📅 Jesus' Age: 12 years old")
                print()
                print("\n📖 KEY VERSE: Luke 2:46-47")
                print('\n💬 "They found him in the temple courts, '
                      'sitting among '
                      'the teachers, listening to them and asking '
                      'them '
                      'questions. Everyone who heard him was amazed '
                      'at his '
                      'understanding and his answers."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Revealed Jesus' divine wisdom even as a "
                      "child.")
                print("   Even as a boy, Jesus showed His divine "
                      "nature.")
                print()
                print('\n💡 "Why were you searching for me? Didn\'t '
                      'you know '
                      'I had to be in my Father\'s house?" - '
                      'Luke 2:49')
                print()
                print("\n🙏 Even as a child, Jesus knew His divine "
                      "purpose!")
                input("\nPress Enter to continue...")

            # Moment 4
            elif option == "4":
                print("=" * 70)
                print(f"\n💧 Public Ministry Begins: "
                      f"{jesus_moments.moment4_formatted}")
                print("=" * 70)
                print("\n📍 Location: Jordan River")
                print("\n👥 Key People: Jesus, John the Baptist")
                print("\n📅 Time: Approximately AD 26")
                print()
                print("\n📖 KEY VERSE: Matthew 3:16")
                print('\n💬 "As soon as Jesus was baptized, he went '
                      'up out of '
                      'the water. At that moment heaven was opened, '
                      'and '
                      'he saw the Spirit of God descending like a '
                      'dove."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Inaugurated Jesus' public ministry with "
                      "divine affirmation.")
                print("   The Trinity is revealed in this pivotal "
                      "moment.")
                print()
                print("\n💡 GOD'S VOICE FROM HEAVEN:")
                print('   "This is my Son, whom I love; with him I '
                      'am well pleased." - Matthew 3:17')
                print()
                print("\n🙏 May we seek God's approval in all we do!")
                input("\nPress Enter to continue...")

            # Moment 5
            elif option == "5":
                print("=" * 70)
                print(f"\n🛡 Victory Over Sin: "
                      f"{jesus_moments.moment5_formatted}")
                print("=" * 70)
                print("\n📍 Location: Wilderness")
                print("\n👥 Key People: Jesus, the devil")
                print("\n📅 Time: Approximately AD 26")
                print()
                print("\n📖 KEY VERSE: Matthew 4:1")
                print('\n💬 "Then Jesus was led by the Spirit into '
                      'the wilderness '
                      'to be tempted by the devil."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Demonstrated Jesus' obedience and reliance "
                      "on Scripture.")
                print("   Jesus resisted temptation using God's "
                      "Word.")
                print()
                print("\n💡 JESUS' RESPONSE TO TEMPTATION:")
                print('   "It is written: \'Man shall not live on '
                      'bread alone...\'" - Matthew 4:4')
                print()
                print("\n🙏 Let us arm ourselves with Scripture "
                      "against trials!")
                input("\nPress Enter to continue...")

            # Moment 6
            elif option == "6":
                print("=" * 70)
                print(f"\n👥 Building the Team: "
                      f"{jesus_moments.moment6_formatted}")
                print("=" * 70)
                print("\n📍 Location: Near Jordan River")
                print("\n👥 Key People: Jesus, John, Andrew, Peter, "
                      "Philip, Nathanael")
                print("\n📅 Time: Approximately AD 26")
                print()
                print("\n📖 KEY VERSE: John 1:35-36")
                print('\n💬 "The next day John was there again with '
                      'two of his '
                      'disciples. When he saw Jesus passing by, he '
                      'said, '
                      '\'Look, the Lamb of God!\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Began gathering followers who would spread "
                      "the Gospel.")
                print("   The foundation of the early church was "
                      "laid.")
                print()
                print("\n💡 DISCIPLES' EXCITEMENT:")
                print('   "We have found the one Moses wrote '
                      'about..." - John 1:45')
                print()
                print("\n🙏 May we follow Jesus with the same zeal!")
                input("\nPress Enter to continue...")

            # Moment 7
            elif option == "7":
                print("=" * 70)
                print(f"\n🍷 Sign of Glory: "
                      f"{jesus_moments.moment7_formatted}")
                print("=" * 70)
                print("\n📍 Location: Cana")
                print("\n👥 Key People: Jesus, Mary, servants")
                print("\n📅 Time: Approximately AD 27")
                print()
                print("\n📖 KEY VERSE: John 2:7-8")
                print('\n💬 "Jesus said to the servants, \'Fill the '
                      'jars with water\'; '
                      'so they filled them to the brim. Then he told '
                      'them, '
                      '\'Now draw some out and take it to the master '
                      'of the banquet.\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Revealed Jesus' glory and strengthened the "
                      "disciples' faith.")
                print("   Water turned to wine, a sign of "
                      "abundance.")
                print()
                print("\n💡 MARY'S WORDS:")
                print('   "Do whatever he tells you." - John 2:5')
                print()
                print("\n🙏 Obey Jesus in every situation!")
                input("\nPress Enter to continue...")

            # Moment 8
            elif option == "8":
                print("=" * 70)
                print(f"\n🛏 Authority Over Sin: "
                      f"{jesus_moments.moment8_formatted}")
                print("=" * 70)
                print("\n📍 Location: Capernaum")
                print("\n👥 Key People: Jesus, paralyzed man, "
                      "friends, scribes")
                print("\n📅 Time: Approximately AD 28")
                print()
                print("\n📖 KEY VERSE: Luke 5:18")
                print('\n💬 "Some men came carrying a paralyzed man '
                      'on a mat and '
                      'tried to take him into the house to lay him '
                      'before Jesus."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Demonstrated Jesus' power to forgive sins "
                      "and heal bodies.")
                print("   Faith of friends led to healing.")
                print()
                print("\n💡 JESUS' WORDS:")
                print('   "Friend, your sins are forgiven." - '
                      'Luke 5:20')
                print()
                print("\n🙏 Bring others to Jesus in faith!")
                input("\nPress Enter to continue...")

            # Moment 9
            elif option == "9":
                print("=" * 70)
                print(f"\n⛈ Power Over Nature: "
                      f"{jesus_moments.moment9_formatted}")
                print("=" * 70)
                print("\n📍 Location: Sea of Galilee")
                print("\n👥 Key People: Jesus, disciples")
                print("\n📅 Time: Approximately AD 28")
                print()
                print("\n📖 KEY VERSE: Matthew 8:23-24")
                print('\n💬 "Then he got into the boat and his '
                      'disciples followed him. '
                      'Suddenly a furious storm came up on the lake, '
                      'so that the '
                      'waves swept over the boat."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Showed Jesus' authority over creation and "
                      "taught faith.")
                print("   'Why are you so afraid?' Jesus asked.")
                print()
                print("\n💡 DISCIPLES' FEAR:")
                print('   "Lord, save us! We\'re going to drown!" - '
                      'Matthew 8:25')
                print()
                print("\n🙏 Trust Jesus in life's storms!")
                input("\nPress Enter to continue...")

            # Moment 10
            elif option == "10":
                print("=" * 70)
                print(f"\n🍞 Miracle of Provision: "
                      f"{jesus_moments.moment10_formatted}")
                print("=" * 70)
                print("\n📍 Location: Near Sea of Galilee")
                print("\n👥 Key People: Jesus, disciples, crowd of "
                      "5000 men")
                print("\n📅 Time: Approximately AD 28")
                print()
                print("\n📖 KEY VERSE: Matthew 14:19")
                print('\n💬 "Taking the five loaves and the two fish '
                      'and looking up '
                      'to heaven, he gave thanks and broke the '
                      'loaves. Then he '
                      'gave them to the disciples..."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Affirmed Jesus as the provider and "
                      "foreshadowed the Eucharist.")
                print("   Abundance from scarcity.")
                print()
                print("\n💡 THE REMAINDER:")
                print("   Twelve basketfuls of broken pieces. - "
                      "Matthew 14:20")
                print()
                print("\n🙏 God provides more than enough!")
                input("\nPress Enter to continue...")
            # Moment 11
            elif option == "11":
                print("=" * 70)
                print(f"\n🌊 Master of the Sea: "
                      f"{jesus_moments.moment11_formatted}")
                print("=" * 70)
                print("\n📍 Location: Sea of Galilee")
                print("\n👥 Key People: Jesus, disciples (including "
                      "Peter)")
                print("\n📅 Time: Approximately AD 28")
                print()
                print("\n📖 KEY VERSE: Matthew 14:25-26")
                print('\n💬 "During the fourth watch of the night '
                      'Jesus went out to '
                      'them, walking on the lake. When the disciples '
                      'saw him '
                      'walking on the lake, they were terrified."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Demonstrated Jesus' divine power and "
                      "Peter's brief faith.")
                print("   'It is I; don't be afraid.'")
                print()
                print("\n💡 PETER'S BOLD STEP:")
                print('   "Lord, if it\'s you, tell me to come to '
                      'you on the water." - Matthew 14:28')
                print()
                print("\n🙏 Step out in faith toward Jesus!")
                input("\nPress Enter to continue...")

            # Moment 12
            elif option == "12":
                print("=" * 70)
                print(f"\n⚰ Victory Over Death: "
                      f"{jesus_moments.moment12_formatted}")
                print("=" * 70)
                print("\n📍 Location: Bethany")
                print("\n👥 Key People: Jesus, Lazarus, Mary, Martha")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: John 11:43-44")
                print('\n💬 "Jesus called in a loud voice, \'Lazarus, '
                      'come out!\' '
                      'The dead man came out, his hands and feet '
                      'wrapped '
                      'with strips of linen..."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Powerful sign pointing to Jesus' own "
                      "resurrection.")
                print("   'I am the resurrection and the life.'")
                print()
                print("\n💡 MARTHA'S CONFESSION:")
                print('   "I believe that you are the Messiah, the '
                      'Son of God." - John 11:27')
                print()
                print("\n🙏 Believe in Jesus, the giver of life!")
                input("\nPress Enter to continue...")

            # Moment 13
            elif option == "13":
                print("=" * 70)
                print(f"\n👁 Light of the World: "
                      f"{jesus_moments.moment13_formatted}")
                print("=" * 70)
                print("\n📍 Location: Jerusalem")
                print("\n👥 Key People: Jesus, blind man, Pharisees")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: John 9:25")
                print('\n💬 "He replied, \'Whether he is a sinner or '
                      'not, I don\'t know. '
                      'One thing I do know. I was blind but now I '
                      'see!\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Revealed Jesus as the light and led to "
                      "bold testimony.")
                print("   Simple faith transformed a life.")
                print()
                print("\n💡 BLIND MAN'S TESTIMONY:")
                print('   "If this man were not from God, he could '
                      'do nothing." - John 9:33')
                print()
                print("\n🙏 Share your story of transformation!")
                input("\nPress Enter to continue...")

            # Moment 14
            elif option == "14":
                print("=" * 70)
                print(f"\n⛰ Kingdom Teachings: "
                      f"{jesus_moments.moment14_formatted}")
                print("=" * 70)
                print("\n📍 Location: Mountainside near Sea of "
                      "Galilee")
                print("\n👥 Key People: Jesus, disciples, crowds")
                print("\n📅 Time: Approximately AD 28")
                print()
                print("\n📖 KEY VERSE: Matthew 5:1-2")
                print('\n💬 "Now when Jesus saw the crowds, he went '
                      'up on a mountainside '
                      'and sat down. His disciples came to him, and '
                      'he began to teach them."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Taught kingdom ethics, the Beatitudes, and "
                      "true righteousness.")
                print("   The blueprint for Christian living.")
                print()
                print("\n💡 A BEATITUDE:")
                print('   "Blessed are the poor in spirit, for '
                      'theirs is the kingdom of heaven." - '
                      'Matthew 5:3')
                print()
                print("\n🙏 Live by the Sermon on the Mount!")
                input("\nPress Enter to continue...")

            # Moment 15
            elif option == "15":
                print("=" * 70)
                print(f"\n🏃 Parable of Forgiveness: "
                      f"{jesus_moments.moment15_formatted}")
                print("=" * 70)
                print("\n📍 Location: Not specified")
                print("\n👥 Key People: Jesus (teaching), father, "
                      "prodigal son, older brother")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Luke 15:20")
                print('\n💬 "But while he was still a long way off, '
                      'his father saw him '
                      'and was filled with compassion for him; he '
                      'ran to his son, '
                      'threw his arms around him and kissed him."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Illustrates God's forgiving love and the "
                      "joy of repentance.")
                print("   God's grace runs to the lost.")
                print()
                print("\n💡 FATHER'S JOY:")
                print('   "This son of mine was dead and is alive '
                      'again..." - Luke 15:24')
                print()
                print("\n🙏 Run back to the Father's arms!")
                input("\nPress Enter to continue...")

            # Moment 16
            elif option == "16":
                print("=" * 70)
                print(f"\n🛤 Exclusive Path: "
                      f"{jesus_moments.moment16_formatted}")
                print("=" * 70)
                print("\n📍 Location: Upper room in Jerusalem")
                print("\n👥 Key People: Jesus, disciples")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: John 14:6")
                print('\n💬 "Jesus answered, \'I am the way and the '
                      'truth and the life. '
                      'No one comes to the Father except through '
                      'me.\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Affirms Jesus as the only way to God.")
                print("   Bold claim of divinity.")
                print()
                print("\n💡 COMFORT IN FAREWELL:")
                print('   "Do not let your hearts be troubled." - '
                      'John 14:1')
                print()
                print("\n🙏 Follow the Way today!")
                input("\nPress Enter to continue...")

            # Moment 17
            elif option == "17":
                print("=" * 70)
                print(f"\n❤ Essence of the Law: "
                      f"{jesus_moments.moment17_formatted}")
                print("=" * 70)
                print("\n📍 Location: Jerusalem (Temple)")
                print("\n👥 Key People: Jesus, Pharisees")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Matthew 22:37-38")
                print('\n💬 "Jesus replied: \'Love the Lord your God '
                      'with all your heart '
                      'and with all your soul and with all your '
                      'mind.\' This is '
                      'the first and greatest commandment."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Summarizes all Scripture in love for God "
                      "and neighbor.")
                print("   Love fulfills the law.")
                print()
                print("\n💡 THE SECOND:")
                print('   "Love your neighbor as yourself." - '
                      'Matthew 22:39')
                print()
                print("\n🙏 Love God wholly and others fully!")
                input("\nPress Enter to continue...")

            # Moment 18
            elif option == "18":
                print("=" * 70)
                print(f"\n🐴 Messianic Welcome: "
                      f"{jesus_moments.moment18_formatted}")
                print("=" * 70)
                print("\n📍 Location: Jerusalem")
                print("\n👥 Key People: Jesus, crowds, disciples")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: John 12:12-13")
                print('\n💬 "The next day the great crowd that had '
                      'come for the festival '
                      'heard that Jesus was on his way to Jerusalem. '
                      'They took palm '
                      'branches and went out to meet him, shouting, '
                      '\'Hosanna!\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Fulfilled Zechariah's prophecy of the king "
                      "on a donkey.")
                print("   Joyful yet sorrowful entry.")
                print()
                print("\n💡 CROWD'S PRAISE:")
                print('   "Blessed is he who comes in the name of '
                      'the Lord!" - John 12:13')
                print()
                print("\n🙏 Welcome Jesus as King of your life!")
                input("\nPress Enter to continue...")

            # Moment 19
            elif option == "19":
                print("=" * 70)
                print(f"\n🍞 New Covenant: "
                      f"{jesus_moments.moment19_formatted}")
                print("=" * 70)
                print("\n📍 Location: Upper room in Jerusalem")
                print("\n👥 Key People: Jesus, disciples (including "
                      "Judas)")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Matthew 26:26")
                print('\n💬 "While they were eating, Jesus took '
                      'bread, and when he had '
                      'given thanks, he broke it and gave it to his '
                      'disciples, '
                      'saying, \'Take and eat; this is my body.\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Instituted the Lord's Supper as "
                      "remembrance of his sacrifice.")
                print("   Do this in remembrance of me.")
                print()
                print("\n💡 THE CUP:")
                print('   "This is my blood of the covenant, poured '
                      'out for many." - Matthew 26:28')
                print()
                print("\n🙏 Remember Jesus' sacrifice often!")
                input("\nPress Enter to continue...")

            # Moment 20
            elif option == "20":
                print("=" * 70)
                print(f"\n🌿 Submission to Will: "
                      f"{jesus_moments.moment20_formatted}")
                print("=" * 70)
                print("\n📍 Location: Garden of Gethsemane")
                print("\n👥 Key People: Jesus, disciples (Peter, "
                      "James, John)")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Matthew 26:36")
                print('\n💬 "Then Jesus went with his disciples to a '
                      'place called '
                      'Gethsemane, and he said to them, \'Sit here '
                      'while I go '
                      'over there and pray.\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Jesus submitted to the Father's will amid "
                      "deep sorrow.")
                print("   'Not my will, but yours be done.'")
                print()
                print("\n💡 THE PRAYER:")
                print('   "My Father, if it is possible, may this '
                      'cup be taken from me." - Matthew 26:39')
                print()
                print("\n🙏 Surrender your will to God's!")
                input("\nPress Enter to continue...")

            # Moment 21
            elif option == "21":
                print("=" * 70)
                print(f"\n⚖ Unjust Judgment: "
                      f"{jesus_moments.moment21_formatted}")
                print("=" * 70)
                print("\n📍 Location: Jerusalem (Sanhedrin, Pilate, "
                      "Herod)")
                print("\n👥 Key People: Jesus, Pilate, Caiaphas, "
                      "Herod, Sanhedrin")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Matthew 27:1-2")
                print('\n💬 "Early in the morning, all the chief '
                      'priests and the elders '
                      'of the people made their plans how to have '
                      'Jesus executed. '
                      'So they bound Jesus, led him away and handed '
                      'him over to Pilate."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Unjust trials leading to the cross "
                      "fulfilled prophecy.")
                print("   Silence before accusers.")
                print()
                print("\n💡 PILATE'S QUESTION:")
                print('   "Are you the king of the Jews?" - '
                      'Matthew 27:11')
                print()
                print("\n🙏 Stand firm in truth amid injustice!")
                input("\nPress Enter to continue...")

            # Moment 22
            elif option == "22":
                print("=" * 70)
                print(f"\n✝ Atoning Sacrifice: "
                      f"{jesus_moments.moment22_formatted}")
                print("=" * 70)
                print("\n📍 Location: Golgotha (near Jerusalem)")
                print("\n👥 Key People: Jesus, soldiers, criminals, "
                      "crowds")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Matthew 27:33, 38")
                print('\n💬 "They came to a place called Golgotha '
                      '(which means \'the place '
                      'of the skull\'). There they crucified him, '
                      'and with him two '
                      'robbers, one on his right and one on his '
                      'left."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Jesus' death paid the penalty for our "
                      "sins.")
                print("   The ultimate act of love.")
                print()
                print("\n💡 FROM THE CROSS:")
                print('   "Father, forgive them, for they do not '
                      'know what they are doing." - Luke 23:34')
                print()
                print("\n🙏 Thank God for the cross!")
                input("\nPress Enter to continue...")

            # Moment 23
            elif option == "23":
                print("=" * 70)
                print(f"\n✅ Mission Accomplished: "
                      f"{jesus_moments.moment23_formatted}")
                print("=" * 70)
                print("\n📍 Location: Golgotha (cross)")
                print("\n👥 Key People: Jesus, soldiers")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: John 19:30")
                print('\n💬 "When he had received the drink, Jesus '
                      'said, \'It is finished.\' '
                      'With that, he bowed his head and gave up his '
                      'spirit."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Declared the completion of redemption's "
                      "work.")
                print("   Debt paid in full.")
                print()
                print("\n💡 THE CRY:")
                print('   "Tetelestai - It is finished."')
                print()
                print("\n🙏 Rest in the finished work of Christ!")
                input("\nPress Enter to continue...")

            # Moment 24
            elif option == "24":
                print("=" * 70)
                print(f"\n🌅 Conquest of Death: "
                      f"{jesus_moments.moment24_formatted}")
                print("=" * 70)
                print("\n📍 Location: Tomb near Jerusalem")
                print("\n👥 Key People: Jesus, Mary Magdalene, "
                      "disciples, angels")
                print("\n📅 Time: Approximately AD 30")
                print()
                print("\n📖 KEY VERSE: Matthew 28:5-6")
                print('\n💬 "The angel said to the women, \'Do not '
                      'be afraid, for I know '
                      'that you are looking for Jesus, who was '
                      'crucified. He is '
                      'not here; he has risen, just as he said.\'"')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Victory over sin and death, foundation of "
                      "faith.")
                print("   He is risen indeed!")
                print()
                print("\n💡 ANGEL'S INVITATION:")
                print('   "Come and see the place where he lay." - '
                      'Matthew 28:6')
                print()
                print("\n🙏 Rejoice in the risen Lord!")
                input("\nPress Enter to continue...")

            # Moment 25
            elif option == "25":
                print("=" * 70)
                print(f"\n☁ Return to Glory: "
                      f"{jesus_moments.moment25_formatted}")
                print("=" * 70)
                print("\n📍 Location: Near Bethany")
                print("\n👥 Key People: Jesus, disciples")
                print("\n📅 Time: Approximately AD 30 (40 days after "
                      "resurrection)")
                print()
                print("\n📖 KEY VERSE: Luke 24:51")
                print('\n💬 "While he was blessing them, he left '
                      'them and was taken '
                      'up into heaven."')
                print()
                print("\n🎯 SIGNIFICANCE:")
                print("   Jesus exalted at the Father's right hand, "
                      "sending the Spirit.")
                print("   From earth to throne.")
                print()
                print("\n💡 ANGELS' PROMISE:")
                print('   "This same Jesus... will come back in the '
                      'same way." - Acts 1:11')
                print()
                print("\n🙏 Look up, your redemption draws near!")
                input("\nPress Enter to continue...")

            print("\n--- Enter another number or 'back' to main "
                  "menu! ---")

    # Option 2: The Parables
    # Option 2: The Parables
    elif main_choice == "2":
        while True:
            print("\n" + "=" * 70)
            print("\n📖 THE PARABLES OF JESUS")
            print("=" * 70)
            print("\nLearn from Jesus' teachings:\n")
            print("1 - Parable of the Sower")
            print("2 - Parable of the Good Samaritan")
            print("3 - Parable of the Prodigal Son")
            print("4 - Parable of the Talents")
            print("5 - Parable of the Mustard Seed")
            print("\nType 'back' for main menu or 'quit' to exit")
            print("=" * 70)

            parable_choice = input(
                "\nYour choice (1-5), 'back', or 'quit': "
            ).strip()

            # Quit
            if parable_choice.lower() in ["quit", "q"]:
                verse = random.choice(encouraging_verses)
                print(Fore.CYAN + "\n✝ Thank you for exploring!")
                print(Fore.YELLOW + f"\n🙏 '{verse[1]}'")
                print(Fore.YELLOW + f"   - {verse[0]}")
                exit()

            # Back to main menu
            if parable_choice.lower() in ["back", "b"]:
                break
            # Parable 1: Sower
            if parable_choice == "1":
                print("\n" + "=" * 70)
                print("\n📖 The Parable of the Sower")
                print("=" * 70)
                print("\nA farmer sows seeds on different types of "
                      "soil,")
                print("representing how people receive God's word.")
                print("Some hear and accept it, while others reject "
                      "it.")
                print("\n🌱 'But the seed on good soil stands for "
                      "those with")
                print("   a noble and good heart' - Luke 8:15")
                print("\n💡 Reflect: How do you receive God's word "
                      "in your life?")
                input("\nPress Enter to continue...")

            # Parable 2: Good Samaritan
            elif parable_choice == "2":
                print("\n" + "=" * 70)
                print("\n📖 The Parable of the Good Samaritan")
                print("=" * 70)
                print("\nA man is beaten and left for dead.")
                print("A priest and Levite pass by, but a Samaritan "
                      "helps him,")
                print("showing love and mercy to a stranger.")
                print("\n🤝 'Love your neighbor as yourself.' - "
                      "Luke 10:27")
                print("\n💡 Reflect: Who is your neighbor, and how "
                      "can you show them love?")
                input("\nPress Enter to continue...")

            # Parable 3: Prodigal Son
            elif parable_choice == "3":
                print("\n" + "=" * 70)
                print("\n📖 The Parable of the Prodigal Son")
                print("=" * 70)
                print("\nA son squanders his inheritance but is "
                      "welcomed back by his father,")
                print("illustrating God's forgiving love and joy "
                      "over repentance.")
                print("\n🧑‍🦱 'This son of mine was dead and is alive "
                      "again;' - Luke 15:24")
                print("\n💡 Reflect: Are you in need of forgiveness "
                      "or ready to forgive?")
                input("\nPress Enter to continue...")

            # Parable 4: Talents
            elif parable_choice == "4":
                print("\n" + "=" * 70)
                print("\n📖 The Parable of the Talents")
                print("=" * 70)
                print("\nServants are entrusted with talents (money) "
                      "by their master.")
                print("Two invest and double their amounts, while "
                      "one buries his.")
                print("The master rewards the faithful and punishes "
                      "the lazy.")
                print("\n💰 'Well done, good and faithful servant!' "
                      "- Matthew 25:21")
                print("\n💡 Reflect: How are you using your gifts "
                      "for God's kingdom?")
                input("\nPress Enter to continue...")

            # Parable 5: Mustard Seed
            elif parable_choice == "5":
                print("\n" + "=" * 70)
                print("\n📖 The Parable of the Mustard Seed")
                print("=" * 70)
                print("\nA tiny mustard seed grows into a large "
                      "tree,")
                print("symbolizing how the kingdom of God starts "
                      "small but grows immensely.")
                print("\n🌳 'The kingdom of heaven is like a mustard "
                      "seed...'")
                print("   - Matthew 13:31-32")
                print("\n💡 Reflect: How is your faith growing, even "
                      "from small beginnings?")
                input("\nPress Enter to continue...")

            else:
                print(Fore.RED + f"\n❌ '{parable_choice}' is not "
                      "valid!")
                print("\n💡 Choose 1-5, 'back', or 'quit'")
                continue

            print("\n--- Type another number, 'back' for menu, or "
                  "'quit'! ---")

    # Option 3: Search moments
    # Option 3: Search moments
    elif main_choice == "3":
        while True:
            print("\n" + "=" * 70)
            print("\n🔍 SEARCH MOMENTS BY KEYWORD")
            print("=" * 70)
            print("\nType a keyword (e.g., 'water', 'healing', "
                  "'miracle')")
            print("or 'back' to return to main menu\n")
            print("=" * 70)

            search_term = input("\nEnter keyword or 'back': ").strip()

            # Back to main menu
            if search_term.lower() in ["back", "b"]:
                break

            # Quit
            if search_term.lower() in ["quit", "q"]:
                verse = random.choice(encouraging_verses)
                print(Fore.CYAN + "\n✝ Thank you for exploring the life of "
                      "Jesus!")
                print(Fore.YELLOW + f"\n🙏 '{verse[1]}'")
                print(Fore.YELLOW + f"   - {verse[0]}")
                break
            # Empty search
            if not search_term:
                print(Fore.RED + "\n❌ Please enter a keyword to "
                      "search!")
                continue
            # Search in moments dictionary
            results = []
            for num, moment_dict in moments_data.items():
                # Search in moment title
                if search_term.lower() in moment_dict['title'].lower():
                    results.append((num, moment_dict['title']))

            # Display search results
            if results:
                print(Fore.GREEN + f"\n✅ Found {len(results)} "
                      f"moment(s) matching '{search_term}':\n")
                for num, title in results:
                    print(f"   {num} - {title}")

                print("\n" + "=" * 70)
                choice = input(
                    "\nEnter a number to view details, or 'back' "
                    "to search again: "
                ).strip()

                if choice.lower() in ["back", "b"]:
                    continue

                if choice.lower() in ["quit", "q"]:
                    print(Fore.CYAN + "\n✝ Thank you for "
                          "exploring the life of Jesus!")
                    print(Fore.YELLOW + "\n🙏 'I am with you "
                          "always, to the very end of the age'")
                    print(Fore.YELLOW + "   - Matthew 28:20")
                    exit()

                # Validate number choice
                if (choice.isdigit()
                        and int(choice) in [r[0] for r in results]):
                    print(f"\n💡 Please go to main menu, select "
                          f"option 1, then choose moment {choice}")
                    input("\nPress Enter to continue...")
                else:
                    print(Fore.RED + f"\n❌ '{choice}' is not in "
                          "the search results!")
                    input("\nPress Enter to continue...")
            else:
                print(Fore.RED + f"\n❌ No moments found matching "
                      f"'{search_term}'")
                print("\n💡 Try different keywords like: miracle, "
                      "water, healing, teaching")
                input("\nPress Enter to continue...")

    # Invalid main menu choice
    else:
        print(Fore.RED + f"\n❌ '{main_choice}' is not valid!")
        print("\n💡 Choose 1 (Moments), 2 (Parables), 3 (Search), "
              "or 'quit'")
