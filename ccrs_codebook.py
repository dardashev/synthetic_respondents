# CCRS Codebook dictionary extracted from CCRS Codebook.pdf
ccrs_codebook = {'ResponseID': {'Details': 'Unique respondent identification number', 'Coding': 'Unique alphanumeric combination.'},
 'Language': {'Details': 'Denotes the language of the survey completed\nby the respondent.',
              'Coding': '1 = English\n2 = French\n3 = German\n4 = Arabic\n5 = Portuguese'},
 'ID_Q1': {'Details': 'Country (Numeric)',
           'Coding': '1 = Canada\n'
                     '2 = United States\n'
                     '3 = Germany\n'
                     '4 = Australia\n'
                     '5 = South Africa\n'
                     '6 = Morocco\n'
                     '7 = Lebanon\n'
                     '8 = Brazil'},
 'ID_Q2': {'Details': 'Country (String variable)',
           'Coding': 'Canada\nUnited States\nGermany\nAustralia\nSouth Africa\nMorocco\nLebanon\nBrazil'},
 'ID_Q3': {'Details': 'Age of respondent.', 'Coding': 'Continuous variable (18-99)'},
 'ID_Q4': {'Details': 'Gender of respondent.',
           'Coding': '0 = Female\n1 = Male\n9 = Other / Don’t know / Prefer not to say'},
 'ID_Q5': {'Details': 'Education level of respondent',
           'Coding': '1 = No formal education\n'
                     '2 = Elementary education\n'
                     '3 = Secondary education\n'
                     '4 = College/University education\n'
                     '5 = Postgraduate education'},
 'ID_Q6': {'Details': 'Place of residence: Urban / Rural',
           'Coding': '1 = A big city\n'
                     '2 = A suburb or outskirt of a big city\n'
                     '3 = A town or small city\n'
                     '4 = A village\n'
                     '5 = The countryside\n'
                     '9 = Don’t know / Prefer not to say'},
 'ID_Q7': {'Details': 'Was respondent born in [country in ID_Q1]?', 'Coding': '0 = No\n1 = Yes'},
 'ID_Q8': {'Details': 'Self-described socioeconomic status',
           'Coding': '1 = Lower class\n2 = Middle class\n3 = Upper class'},
 'ID_Q9': {'Details': 'Employment status',
           'Coding': '1 = Working for pay full-time\n'
                     '2 = Working for pay part-time\n'
                     '3 = Retired\n'
                     '4 = Unemployed / looking for work\n'
                     '5 = Student (not working)\n'
                     '9 = Don’t know / prefer not to say / other'},
 'ID_Q10': {'Details': 'Political ideology', 'Coding': 'Continuous variable:\n0 = Left\n10 = Right'},
 'ID_Q11': {'Details': 'Political interest',
            'Coding': 'Continuous variable:\n0 = No interest at all\n10 = A great deal of interest'},
 'ID_Q12': {'Details': 'Did respondent vote in latest national-level\nelection in [country in ID_Q1]?',
            'Coding': '0 = No\n1 = Yes\n9 = Don’t know / Prefer not to answer'},
 'ID_Q13': {'Details': 'Respondent’s self-described likelihood of\n'
                       'voting in next national election in [country in\n'
                       'ID_Q1]',
            'Coding': '0 = Unlikely to vote\n'
                      '1 = Probably will vote\n'
                      '2 = Likely to vote\n'
                      '3 = Certain to vote\n'
                      '9 = Not eligible\n'
                      '99 = Prefer not to say'},
 'ID_Q14_1': {'Details': 'Extent government should [be involved in\nredistribution of wealth]',
              'Coding': 'Continuous variable:\n0 = the least extent\n10 = the greatest extent'},
 'ID_Q14_2': {'Details': 'Extent government should [provide gas and\nfood subsidies]',
              'Coding': 'Continuous variable:\n0 = the least extent\n10 = the greatest extent'},
 'ID_Q14_3': {'Details': 'Extent government should [be focused on\ninstilling discipline]',
              'Coding': 'Continuous variable:\n0 = the least extent\n10 = the greatest extent'},
 'ID_Q14_4': {'Details': 'Extent government should [be involved in\nregulating sexual conduct of individuals]',
              'Coding': 'Continuous variable:\n0 = the least extent\n10 = the greatest extent'},
 'ID_Q14_5': {'Details': 'Extent government should [control\nimmigration]',
              'Coding': 'Continuous variable:\n0 = the least extent\n10 = the greatest extent'},
 'ID_Q15': {'Details': 'Satisfaction with government over past 12\nmonths.',
            'Coding': 'Continuous variable:\n0 = not satisfied at all\n10 = very satisfied'},
 'ID_Q16': {'Details': 'Satisfaction with democracy',
            'Coding': 'Continuous variable:\n0 = not satisfied at all\n10 = very satisfied'},
 'ID_Q17': {'Details': 'Social trust (most people can be trusted)',
            'Coding': '1 = Most people can be trusted\n'
                      '0 = Need to be very careful\n'
                      '9 = Don’t know / prefer not to answer'},
 'ID_Q18_1': {'Details': 'Trust in [the government]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q18_2': {'Details': 'Trust in [politicians]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q18_3': {'Details': 'Trust in [political parties]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q18_4': {'Details': 'Trust in [elections]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q18_5': {'Details': 'Trust in [courts]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q18_6': {'Details': 'Trust in [independent experts]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q18_7': {'Details': 'Trust in [journalists]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q19_1': {'Details': 'How much influence do [bureaucrats] have?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_2': {'Details': 'How much influence do [business leaders]\nhave?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_3': {'Details': 'How much influence do [journalists] have?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_4': {'Details': 'How much influence do [military officers]\nhave?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_5': {'Details': 'How much influence do [politicians] have?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_6': {'Details': 'How much influence do [religious leaders]\nhave?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_7': {'Details': 'How much influence do [scientists] have?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_8': {'Details': 'How much influence do [the wealthy] have?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q19_9': {'Details': 'How much influence do [university\nprofessors] have?',
              'Coding': 'Continuous variable:\n0 = not influential\n10 = highly influential'},
 'ID_Q20_1': {'Details': 'Trust in [bureaucrats]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_2': {'Details': 'Trust in [business leaders]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_3': {'Details': 'Trust in [journalists]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_4': {'Details': 'Trust in [military officers]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_5': {'Details': 'Trust in [politicians]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_6': {'Details': 'Trust in [religious leaders]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_7': {'Details': 'Trust in [scientists]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_8': {'Details': 'Trust in [the wealthy]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q20_9': {'Details': 'Trust in [University professors]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q21_1': {'Details': 'Trust scientists to [competently execute\nresearch]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q21_2': {'Details': 'Trust scientists to [create unbiased\nknowledge]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q21_3': {'Details': 'Trust scientists to [generate useful findings]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q21_4': {'Details': 'Trust scientists to [inform public on important\nissues]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q21_5': {'Details': 'Trust scientists to [provide sound advice to\ngovernment]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_1': {'Details': 'Trust following organization: [Amnesty\nInternational]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_2': {'Details': 'Trust following organization: [Greenpeace]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_3': {'Details': 'Trust following organization: [International\nMonetary Fund]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_4': {'Details': 'Trust following organization: [NATO]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_5': {'Details': 'Trust following organization: [United\nNations]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_6': {'Details': 'Trust following organization: [World Bank]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q22_7': {'Details': 'Trust following organization: [World Health\nOrganization]',
              'Coding': 'Continuous variable:\n0 = no trust at all\n10 = a lot of trust'},
 'ID_Q23': {'Details': 'Populist attitude scale (8-item scale average)\n*Mean score of ID_Q23_1 to ID_Q23_8',
            'Coding': 'Continuous variable:\n1 = Less populist\n5 = More populist'},
 'ID_Q23_1': {'Details': 'The politicians in the [upper house of country\n'
                         'in ID_Q1] need to follow the will of the\n'
                         'people.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_2': {'Details': 'The people, and not politicians, should make\nour most important policy decisions.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_3': {'Details': 'The political differences between the elite and\n'
                         'the people are larger than the differences\n'
                         'among the people.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_4': {'Details': 'I would rather be represented by a citizen than\nby a specialized politician.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_5': {'Details': 'Elected officials talk too much and take too\nlittle action.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_6': {'Details': 'Politics is ultimately a struggle between good\nand evil.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_7': {'Details': 'What people call “compromise” in politics is\nreally just selling out on one’s principles.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q23_8': {'Details': 'Interest groups have too much influence over\npolitical decisions.',
              'Coding': 'Likert scale item:\n1 = Very much disagree\n5 = Very much agree'},
 'ID_Q24': {'Details': 'Religion\n'
                       '**Do not use. Inconsistencies in the coding.\n'
                       'Will be recoded country-by-country to ensure\n'
                       'a universal coding scheme.',
            'Coding': '1 = Muslim\n'
                      '2 = Christian\n'
                      '3 = Jewish\n'
                      '4= Atheist / Non-believer\n'
                      '9 = Other / Don’t know / Prefer not to\n'
                      'answer'},
 'ID_Q25': {'Details': 'Religiosity',
            'Coding': '0 = Not a religious person\n1 = A religious person\n9 = Don’t know / prefer not to answer'},
 'ID_Q26': {'Details': 'Impact of immigrants in [country in ID_Q1]',
            'Coding': 'Continuous variable:\n0 = Very negative impact\n10 = Very positive impact'},
 'ID_Q27': {'Details': 'Authoritarianism (RWA 6-item scale average)',
            'Coding': 'Continuous variable:\n1 = Low RWA\n7 = High RWA'},
 'ID_Q27_1': {'Details': 'Strong, tough government will harm our\ncountry.\n*Reverse-coded',
              'Coding': 'Likert scale item:\n1 = Totally disagree\n7 = Totally agree'},
 'ID_Q27_2': {'Details': 'Being kind to loafers or criminals will only\n'
                         'encourage them to take advantage of your\n'
                         'weakness, so it’s best to use a firm, tough\n'
                         'hand when dealing with them.',
              'Coding': 'Likert scale item:\n1 = Totally disagree\n7 = Totally agree'},
 'ID_Q27_3': {'Details': 'Our society does NOT need tougher\ngovernment and stricter laws.\n*Reverse-coded',
              'Coding': 'Likert scale item:\n1 = Totally disagree\n7 = Totally agree'},
 'ID_Q27_4': {'Details': 'The facts on crime and the recent public\n'
                         'disorders show we have to crack down harder\n'
                         'on troublemakers if we are going preserve law\n'
                         'and order.',
              'Coding': 'Likert scale item:\n1 = Totally disagree\n7 = Totally agree'},
 'ID_Q27_5': {'Details': 'Our prisons are a shocking disgrace. Criminals\n'
                         'are unfortunate people who deserve much\n'
                         'better care, instead of so much punishment.\n'
                         '*Reverse-coded',
              'Coding': 'Likert scale item:\n1 = Totally disagree\n7 = Totally agree'},
 'ID_Q27_6': {'Details': 'The way things are going in this country, it’s\n'
                         'going to take a lot of “strong medicine” to\n'
                         'straighten out the troublemakers, criminals,\n'
                         'and perverts.',
              'Coding': 'Likert scale item:\n1 = Totally disagree\n7 = Totally agree'},
 'ID_Q28_1': {'Details': 'Citizenship norms: importance of\n'
                         'understanding people with different opinions\n'
                         'to be a true [citizenship of country in ID_Q1]',
              'Coding': 'Continuous variable:\n1 = Not at all important\n5 = Very important'},
 'ID_Q28_2': {'Details': 'Citizenship norms: importance of speaking\n'
                         '[language in “language” variable] to be a true\n'
                         '[citizenship of country in ID_Q1]',
              'Coding': 'Continuous variable:\n1 = Not at all important\n5 = Very important'},
 'ID_Q28_3': {'Details': 'Citizenship norms: importance of feeling\n'
                         '[citizenship of country in ID_Q1] to be a true\n'
                         '[citizenship of country in ID_Q1]',
              'Coding': 'Continuous variable:\n1 = Not at all important\n5 = Very important'},
 'ID_Q29': {'Details': 'Cognitive Style (analytical vs. intuitive)*\n'
                       '*this variable represents intuitive thinking\n'
                       'when closer to 0 and analytical thinking when\n'
                       'closer to 3',
            'Coding': 'Sum of Q35_1, Q35_2, and Q35_3:\n'
                      '0 = no answers correct\n'
                      '1 = one answered correctly\n'
                      '2 = two answered correctly\n'
                      '3 = all answers correct'},
 'ID_Q29_1': {'Details': 'Cognitive reflection task #1', 'Coding': '0 = intuitive answer\n1 = analytical answer'},
 'ID_Q29_2': {'Details': 'Cognitive reflection task #2', 'Coding': '0 = intuitive answer\n1 = analytical answer'},
 'ID_Q29_3': {'Details': 'Cognitive reflection task #3', 'Coding': '0 = intuitive answer\n1 = analytical answer'},
 'ID_Q30': {'Details': 'Need for cognitive closure (15-item scale\naverage)\n*Mean score of ID_Q38_1 to ID_Q38_15',
            'Coding': 'Continuous variable:\n1 = Low need for cognitive closure\n5 = High need for cognitive closure'},
 'ID_Q30_1': {'Details': 'I don’t like situations that are uncertain.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_2': {'Details': 'I dislike questions which could be answered in\nmany different ways.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_3': {'Details': 'I find that a well-ordered life with regular\nhours suits my temperament.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_4': {'Details': 'I feel uncomfortable when I don’t understand\nthe reason why an event occurred in my life.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_5': {'Details': 'I feel irritated when one person disagrees with\nwhat everyone else in a group believes.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_6': {'Details': 'I don’t like to go into a situation without\nknowing what I can expect from it.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_7': {'Details': 'When I have made a decision, I feel relieved.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_8': {'Details': 'When I am confronted with a problem, I’m\ndying to reach a solution very quickly.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_9': {'Details': 'I would quickly become impatient and\n'
                         'irritated if I would not find a solution to a\n'
                         'problem immediately.',
              'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_10': {'Details': 'I don’t like to be with people who are capable\nof unexpected actions.',
               'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_11': {'Details': 'I dislike it when a person’s statement could\nmean many different things.',
               'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_12': {'Details': 'I find that establishing a consistent routine\nenables me to enjoy life more.',
               'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_13': {'Details': 'I enjoy having a clear and structured mode of\nlife.',
               'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_14': {'Details': 'I do not usually consult many different\nopinions before forming my own view.',
               'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q30_15': {'Details': 'I dislike unpredictable situations.',
               'Coding': 'Likert scale item:\n1 = Completely disagree\n5 = Completely agree'},
 'ID_Q31': {'Details': 'Self-esteem scale (10-item scale average)',
            'Coding': 'Continuous variable:\n0 = Low self-esteem\n3 = High self-esteem'},
 'ID_Q31_1': {'Details': 'I feel that I am a person of worth, at least on\nan equal plane with others.',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_2': {'Details': 'I feel that I have a number of good qualities.',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_3': {'Details': 'All in all, I am inclined to feel that I am a\nfailure.\n*Reverse-coded',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_4': {'Details': 'I am able to do things as well as most people.',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_5': {'Details': 'I feel I do not have much to be proud of.\n*Reverse-coded',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_6': {'Details': 'I take a positive attitude towards myself.',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_7': {'Details': 'On the whole, I am satisfied with myself.',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_8': {'Details': 'I wish I could have more respect for myself.\n*Reverse-coded',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_9': {'Details': 'I certainly feel useless at times.\n*Reverse-coded',
              'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q31_10': {'Details': 'At times I think that I am not good at all.\n*Reverse-coded',
               'Coding': 'Likert scale item:\n0 = Does not apply to me\n3 = Applies to me'},
 'ID_Q32': {'Details': 'Conspiracy belief scale (14-item scale\naverage)',
            'Coding': 'Continuous variable:\n0 = Low conspiracy beliefs\n4 = High conspiracy beliefs'},
 'ID_Q32_1': {'Details': 'The government is involved in the murder of\n'
                         'innocent citizens and/or well-known public\n'
                         'figures and keeps this a secret.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_2': {'Details': 'The power held by heads of state is second to\n'
                         'that of small unknown groups who really\n'
                         'control world politics.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_3': {'Details': 'Secret organizations communicate with\n'
                         'extraterrestrials but keep this fact from the\n'
                         'public.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_4': {'Details': 'The spread of certain viruses and/or diseases\n'
                         'is the result of the deliberate, concealed efforts\n'
                         'of some organization.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_5': {'Details': 'Groups of scientists manipulate, fabricate, or\n'
                         'suppress evidence in order to deceive the\n'
                         'public.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_6': {'Details': 'The government permits or perpetrates acts of\n'
                         'terrorism on its own soil, disguising its\n'
                         'involvement.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_7': {'Details': 'A small, secret group of people is responsible\n'
                         'for making all major world decisions, such as\n'
                         'going to war.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_8': {'Details': 'Evidence of alien contact is being concealed\nfrom the public.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_9': {'Details': 'Technology with mind-control capacities is\nused on people without their knowledge.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_10': {'Details': 'The government uses people as patsies to hide\nits involvement in criminal activity.',
               'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_11': {'Details': 'Certain significant events have been the result\n'
                          'of the activity of a small group who secretly\n'
                          'manipulate world events.',
               'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_12': {'Details': 'Some UFO sightings and rumors are planned\n'
                          'or staged in order to distract the public from\n'
                          'real alien contact.',
               'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_13': {'Details': 'Experiments involving new drugs or\n'
                          'technologies are routinely carried out on the\n'
                          'public without their knowledge or consent.',
               'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q32_14': {'Details': 'A lot of important information is deliberately\n'
                          'concealed from the public out of self-interest.',
               'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q33': {'Details': 'Conspiracy Mentality Scale (5-item scale\naverage)',
            'Coding': 'Continuous variable:\n0 = Low conspiracy mentality\n10 = High conspiracy mentality'},
 'ID_Q33_1': {'Details': 'Many very important things happen in the\nworld, which the public is never informed\nabout.',
              'Coding': 'Likert scale item:\n0 = Certainly not\n10 = Certain'},
 'ID_Q33_2': {'Details': 'Politicians usually do not tell us the true\nmotives for their decisions.',
              'Coding': 'Likert scale item:\n0 = Certainly not\n10 = Certain'},
 'ID_Q33_3': {'Details': 'Government agencies closely monitor all\ncitizens.',
              'Coding': 'Likert scale item:\n0 = Certainly not\n10 = Certain'},
 'ID_Q33_4': {'Details': 'Events which superficially seem to lack a\n'
                         'connection are often the result of secret\n'
                         'activities.',
              'Coding': 'Likert scale item:\n0 = Certainly not\n10 = Certain'},
 'ID_Q33_5': {'Details': 'There are secret organizations that greatly\ninfluence political decisions.',
              'Coding': 'Likert scale item:\n0 = Certainly not\n10 = Certain'},
 'ID_Q34': {'Details': 'Activism Intention Scale (4-item scale\naverage)',
            'Coding': 'Continuous variable:\n0 = Lower intentions\n10 = Higher intentions'},
 'ID_Q34_1': {'Details': 'I would join/belong to an organization that\n'
                         'fights for my group’s political and legal rights.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q34_2': {'Details': 'I would donate money to an organization that\n'
                         'fights for my group’s political and legal rights.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q34_3': {'Details': 'I would volunteer my time working (i.e., write\n'
                         'petitions, distribute flyers, recruit people, etc.)\n'
                         'for an organization that fights for my group’s\n'
                         'political and legal rights.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q34_4': {'Details': 'I would travel for one hour to join in a public\n'
                         'rally, protest, or demonstration in support of\n'
                         'my group.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q35': {'Details': 'Radicalism Intention Scale (4-item scale\naverage)',
            'Coding': 'Continuous variable:\n0 = Lower intentions\n10 = Higher intentions'},
 'ID_Q35_1': {'Details': 'I would continue to support an organization\n'
                         'that fights for my group’s political and legal\n'
                         'rights even if the organization sometimes\n'
                         'breaks the law.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q35_2': {'Details': 'I would continue to support an organization\n'
                         'that fights for my group’s political and legal\n'
                         'rights even if the organization sometimes\n'
                         'resorts to violence.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q35_3': {'Details': 'I would participate in a public protest against\n'
                         'oppression of my group even if I thought the\n'
                         'protest might turn violent.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q35_4': {'Details': 'I would attack police or security forces if I\nsaw them beating members of my group.',
              'Coding': 'Likert scale item:\n0 = Strongly disagree\n10 = Strongly agree'},
 'ID_Q36_1': {'Details': 'Canada: Liberals and environmental actors are\n'
                         'working together to destroy Alberta’s oil\n'
                         'sands for financial benefit.\n'
                         'United States: The US government had\n'
                         'something to do with the attacks of 9/11.\n'
                         'Germany: The Jewish population was\n'
                         'responsible for starting World War II, not the\n'
                         'Nazi party of Germany.\n'
                         'Australia: The Chinese government had\n'
                         'something to do with the disappearance of\n'
                         'Prime Minister Harold Holt\n'
                         'South Africa: AIDS was created by white\n'
                         'people to kill Black people.\n'
                         'Morocco: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'Lebanon: The Beirut explosion was not an\n'
                         'accident.\n'
                         'Brazil: The 2022 Election was fraudulent, and\n'
                         'Jair Bolsonaro is the true winner.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_2': {'Details': 'Canada: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'United States: Bill Gates and George Soros\n'
                         'are responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'Germany: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'Australia: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'South Africa: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'Morocco: The pandemic is being used by a\n'
                         'small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'Lebanon: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.\n'
                         'Brazil: Bill Gates and George Soros are\n'
                         'responsible for the onset of the Covid-19\n'
                         'pandemic.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_3': {'Details': 'Canada: Liberal media are paid actors\n'
                         'working for Prime Minister Justin Trudeau.\n'
                         'United States: Joe Biden did not legitimately\n'
                         'win the 2020 US Presidential Election.\n'
                         'Germany: Hitler did not die in 1945, but\n'
                         'rather, lived into his old age.\n'
                         'Australia: Pedophilic Satan-worshiping elites\n'
                         'are trying to control our media and politics\n'
                         'South Africa: Birth control and condoms were\n'
                         'created to control the Black population and\n'
                         'should not be used.\n'
                         'Morocco: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'Lebanon: The assassination of Rafic Hariri is\n'
                         'related to the Beirut explosion.\n'
                         'Brazil: The pandemic is being used by a small\n'
                         'group of elites to swap capitalism for\n'
                         'communism in liberal democracies.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_4': {'Details': 'Canada: The pandemic is being used by a\n'
                         'small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'United States: There is more to the\n'
                         'assassination of President John F. Kennedy\n'
                         'that what has been shared with the public.\n'
                         'Germany: The pandemic is being used by a\n'
                         'small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'Australia: The pandemic is being used by a\n'
                         'small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'South Africa: The pandemic is being used by\n'
                         'a small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'Morocco: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.\n'
                         'Lebanon: The pandemic is being used by a\n'
                         'small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'Brazil: Climate change is a hoax and scientists\n'
                         'touting its existence are lying.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_5': {'Details': 'Canada: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'United States: Area 51 is home to more than\n'
                         'just a simple US Air Force base.\n'
                         'Germany: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'Australia: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'South Africa: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'Lebanon: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'Brazil: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_6': {'Details': 'Canada: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.\n'
                         'United States: Former President Barack\n'
                         'Obama is lying about his birthplace.\n'
                         'Germany: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.\n'
                         'Australia: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.\n'
                         'South Africa: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.\n'
                         'Lebanon: The pharmaceutical industry has\n'
                         'orchestrated the spread of the Sars-Cov-2 and\n'
                         'Monkeypox viruses for its own financial\n'
                         'benefit.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_7': {'Details': 'Canada: Pierre Poilievre is a Russian Agent\n'
                         'sent to Canada to polarize politics.\n'
                         'United States: The pandemic is being used by\n'
                         'a small group of elites to swap capitalism for\n'
                         'communism in liberal democracies.\n'
                         'Germany: Secret powers, like the CIA or\n'
                         'billionaire families, control the world.\n'
                         'Australia: Secret powers, like the CIA or\n'
                         'billionaire families, control the world.\n'
                         'South Africa: The government and scientists\n'
                         'have a cure for HIV/AIDS, but they are hiding\n'
                         'it.\n'
                         'Lebanon: The Israeli government has\n'
                         'something to do with the Beirut explosion.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_8': {'Details': 'United States: Climate change is a hoax and\n'
                         'scientists touting its existence are lying.\n'
                         'Germany: Past NATO operations in Germany\n'
                         'were an operation by President Trump to\n'
                         'liberate Germany from Chancellor Angela\n'
                         'Merkel.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'},
 'ID_Q36_9': {'Details': 'United States: The pharmaceutical industry\n'
                         'has orchestrated the spread of the Sars-Cov-2\n'
                         'and Monkeypox viruses for its own financial\n'
                         'benefit.',
              'Coding': 'Likert scale item:\n0 = Definitely not true\n4= Definitely true'}}
