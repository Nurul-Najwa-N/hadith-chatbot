# ── Islamic Named Entities for NER ───────────────────────────────────────────
# Used by fuzzy matching and entity extraction pipeline
# Demonstrates NER capability from FYP research

ISLAMIC_ENTITIES = {
    "Prophet Muhammad": ["muhammad", "prophet", "messenger", "rasulullah", "rasul", "nabi", "mohammed", "muhammed", "pbuh"],
    "Allah": ["allah", "god", "lord", "almighty", "creator"],
    "Abu Bakr": ["abu bakr", "abu baker", "abubakar", "siddiq"],
    "Umar": ["umar", "omar", "umar ibn khattab", "al-faruq"],
    "Uthman": ["uthman", "othman", "uthman ibn affan"],
    "Ali": ["ali", "ali ibn abi talib", "abu turab"],
    "Aisha": ["aisha", "aishah", "aisha bint abi bakr", "mother of believers"],
    "Prayer": ["salah", "salat", "prayer", "namaz", "salaah", "solat"],
    "Fasting": ["sawm", "fasting", "ramadan", "siyam", "puasa"],
    "Zakat": ["zakat", "zakah", "charity", "alms", "sadaqah"],
    "Hajj": ["hajj", "pilgrimage", "haj", "mecca", "kabah", "kaaba"],
    "Quran": ["quran", "quran", "koran", "scripture", "al-quran"],
    "Paradise": ["jannah", "paradise", "heaven", "garden"],
    "Hellfire": ["jahannam", "hellfire", "hell", "fire"],
    "Angels": ["angel", "malaika", "jibril", "gabriel", "jibreel"],
    "Knowledge": ["knowledge", "ilm", "learning", "education", "scholar"],
    "Patience": ["sabr", "patience", "perseverance", "steadfast"],
    "Gratitude": ["shukr", "gratitude", "thankfulness", "grateful"],
    "Honesty": ["sidq", "honesty", "truthfulness", "truth", "honest"],
    "Justice": ["adl", "justice", "fairness", "equity"],
    "Kindness": ["kindness", "mercy", "rahma", "compassion", "gentle"],
    "Parents": ["parents", "mother", "father", "walid", "walidain"],
    "Neighbours": ["neighbour", "neighbor", "jar"],
    "Cleanliness": ["cleanliness", "taharah", "purity", "wudu", "ablution"],
    "Death": ["death", "maut", "akhirah", "afterlife", "grave"],
}

# ── Hadith Dataset ────────────────────────────────────────────────────────────
# Authentic Hadiths from major collections (public domain)
# Sourced from: sunnah.com (open access)

HADITH_DATASET = [
    # KINDNESS & MERCY
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 26",
        "text": "The Prophet (ﷺ) said: 'He who is not merciful to others, will not be treated mercifully.'",
        "arabic": "لَا يَرْحَمُ اللَّهُ مَنْ لَا يَرْحَمُ النَّاسَ",
        "narrator": "Jarir ibn Abdullah",
        "topics": ["mercy", "kindness", "compassion"]
    },
    {
        "collection": "Sahih Muslim",
        "reference": "Book 45, Hadith 87",
        "text": "The Prophet (ﷺ) said: 'Show mercy to those on earth and the One in heaven will show mercy to you.'",
        "arabic": "ارْحَمُوا مَنْ فِي الْأَرْضِ يَرْحَمْكُمْ مَنْ فِي السَّمَاءِ",
        "narrator": "Abdullah ibn Amr",
        "topics": ["mercy", "kindness", "Allah"]
    },
    # PARENTS
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 2",
        "text": "A man asked the Prophet (ﷺ): 'Who is most deserving of my good companionship?' The Prophet said: 'Your mother.' The man asked: 'Then who?' He said: 'Your mother.' The man asked: 'Then who?' He said: 'Your mother.' The man asked again: 'Then who?' He said: 'Your father.'",
        "arabic": "أُمُّكَ ثُمَّ أُمُّكَ ثُمَّ أُمُّكَ ثُمَّ أَبُوكَ",
        "narrator": "Abu Huraira",
        "topics": ["parents", "mother", "father", "rights", "kindness"]
    },
    {
        "collection": "Sunan Abu Dawud",
        "reference": "Book 41, Hadith 5120",
        "text": "The Prophet (ﷺ) said: 'The Lord's pleasure is in the parent's pleasure, and the Lord's anger is in the parent's anger.'",
        "arabic": "رِضَا الرَّبِّ فِي رِضَا الْوَالِدِ وَسَخَطُ الرَّبِّ فِي سَخَطِ الْوَالِدِ",
        "narrator": "Abdullah ibn Amr",
        "topics": ["parents", "respect", "obedience", "Allah"]
    },
    # KNOWLEDGE
    {
        "collection": "Sunan Ibn Majah",
        "reference": "Book 1, Hadith 224",
        "text": "The Prophet (ﷺ) said: 'Seeking knowledge is an obligation upon every Muslim.'",
        "arabic": "طَلَبُ الْعِلْمِ فَرِيضَةٌ عَلَى كُلِّ مُسْلِمٍ",
        "narrator": "Anas ibn Malik",
        "topics": ["knowledge", "learning", "education", "obligation"]
    },
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 3, Hadith 71",
        "text": "The Prophet (ﷺ) said: 'If Allah wants to do good for someone, He makes him comprehend the religion.'",
        "arabic": "مَنْ يُرِدِ اللَّهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّينِ",
        "narrator": "Muawiyah",
        "topics": ["knowledge", "religion", "Allah", "blessing"]
    },
    # HONESTY
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 116",
        "text": "The Prophet (ﷺ) said: 'Truthfulness leads to righteousness and righteousness leads to Paradise. A man keeps on telling the truth until he becomes a truthful person. Falsehood leads to wickedness and wickedness leads to Hellfire.'",
        "arabic": "عَلَيْكُمْ بِالصِّدْقِ فَإِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ",
        "narrator": "Abdullah ibn Masud",
        "topics": ["honesty", "truth", "paradise", "hellfire", "righteousness"]
    },
    {
        "collection": "Sahih Muslim",
        "reference": "Book 32, Hadith 6219",
        "text": "The Prophet (ﷺ) said: 'It is obligatory for you to tell the truth, for truth leads to virtue and virtue leads to Paradise.'",
        "arabic": "عَلَيْكُمْ بِالصِّدْقِ",
        "narrator": "Ibn Masud",
        "topics": ["honesty", "truth", "virtue", "paradise"]
    },
    # PATIENCE
    {
        "collection": "Sahih Muslim",
        "reference": "Book 47, Hadith 53",
        "text": "The Prophet (ﷺ) said: 'How wonderful is the case of a believer; there is good for him in everything and this applies only to a believer. If prosperity attends him, he expresses gratitude to Allah and that is good for him; and if adversity befalls him, he endures it patiently and that is also good for him.'",
        "arabic": "عَجَبًا لِأَمْرِ الْمُؤْمِنِ إِنَّ أَمْرَهُ كُلَّهُ خَيْرٌ",
        "narrator": "Suhaib",
        "topics": ["patience", "gratitude", "believer", "prosperity", "adversity"]
    },
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 70, Hadith 545",
        "text": "The Prophet (ﷺ) said: 'No fatigue, nor disease, nor sorrow, nor sadness, nor hurt, nor distress befalls a Muslim, even if it were the prick he receives from a thorn, but that Allah expiates some of his sins for that.'",
        "arabic": "مَا يُصِيبُ الْمُسْلِمَ مِنْ نَصَبٍ وَلَا وَصَبٍ",
        "narrator": "Abu Said and Abu Huraira",
        "topics": ["patience", "suffering", "sins", "expiation", "Allah"]
    },
    # CLEANLINESS
    {
        "collection": "Sahih Muslim",
        "reference": "Book 2, Hadith 432",
        "text": "The Prophet (ﷺ) said: 'Cleanliness is half of faith.'",
        "arabic": "الطُّهُورُ شَطْرُ الْإِيمَانِ",
        "narrator": "Abu Malik al-Ash'ari",
        "topics": ["cleanliness", "purity", "faith", "taharah"]
    },
    {
        "collection": "Sunan Abu Dawud",
        "reference": "Book 1, Hadith 3",
        "text": "The Prophet (ﷺ) said: 'Allah does not accept prayer without purification.'",
        "arabic": "لَا يَقْبَلُ اللَّهُ صَلَاةً بِغَيْرِ طُهُورٍ",
        "narrator": "Abu Huraira",
        "topics": ["cleanliness", "prayer", "wudu", "ablution", "purity"]
    },
    # PRAYER
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 8, Hadith 330",
        "text": "The Prophet (ﷺ) said: 'The key to Paradise is prayer and the key to prayer is cleanliness.'",
        "arabic": "مِفْتَاحُ الْجَنَّةِ الصَّلَاةُ وَمِفْتَاحُ الصَّلَاةِ الطُّهُورُ",
        "narrator": "Jabir ibn Abdullah",
        "topics": ["prayer", "paradise", "cleanliness", "key"]
    },
    {
        "collection": "Sahih Muslim",
        "reference": "Book 4, Hadith 1381",
        "text": "The Prophet (ﷺ) said: 'The first matter that the slave will be brought to account for on the Day of Judgment is the prayer. If it is sound, then the rest of his deeds will be sound. And if it is corrupt, then the rest of his deeds will be corrupt.'",
        "arabic": "أَوَّلُ مَا يُحَاسَبُ بِهِ الْعَبْدُ الصَّلَاةُ",
        "narrator": "Abu Huraira",
        "topics": ["prayer", "judgment day", "deeds", "accountability"]
    },
    # NEIGHBOURS
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 43",
        "text": "The Prophet (ﷺ) said: 'By Allah, he does not believe! By Allah, he does not believe! By Allah, he does not believe!' It was asked: 'Who is that, O Allah's Messenger?' He said: 'That person whose neighbour does not feel safe from his evil.'",
        "arabic": "وَاللَّهِ لَا يُؤْمِنُ وَاللَّهِ لَا يُؤْمِنُ وَاللَّهِ لَا يُؤْمِنُ",
        "narrator": "Abu Huraira",
        "topics": ["neighbours", "faith", "evil", "safety", "belief"]
    },
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 45",
        "text": "The Prophet (ﷺ) said: 'Jibril kept recommending treating neighbours with kindness until I thought he would assign them a share of inheritance.'",
        "arabic": "مَا زَالَ جِبْرِيلُ يُوصِينِي بِالْجَارِ",
        "narrator": "Aisha and Ibn Umar",
        "topics": ["neighbours", "kindness", "jibril", "rights", "angel"]
    },
    # CHARITY
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 24, Hadith 501",
        "text": "The Prophet (ﷺ) said: 'The upper hand is better than the lower hand (i.e. he who gives in charity is better than him who takes it).'",
        "arabic": "الْيَدُ الْعُلْيَا خَيْرٌ مِنَ الْيَدِ السُّفْلَى",
        "narrator": "Ibn Umar",
        "topics": ["charity", "giving", "sadaqah", "generosity"]
    },
    {
        "collection": "Sahih Muslim",
        "reference": "Book 12, Hadith 71",
        "text": "The Prophet (ﷺ) said: 'Charity does not in any way decrease the wealth and the servant who forgives, Allah adds to his respect; and the one who shows humility, Allah elevates him in the estimation of the people.'",
        "arabic": "مَا نَقَصَتْ صَدَقَةٌ مِنْ مَالٍ",
        "narrator": "Abu Huraira",
        "topics": ["charity", "wealth", "forgiveness", "humility", "Allah"]
    },
    # JUSTICE
    {
        "collection": "Sahih Muslim",
        "reference": "Book 32, Hadith 6248",
        "text": "The Prophet (ﷺ) said: 'Beware of oppression, for oppression will be darkness on the Day of Resurrection.'",
        "arabic": "اتَّقُوا الظُّلْمَ فَإِنَّ الظُّلْمَ ظُلُمَاتٌ يَوْمَ الْقِيَامَةِ",
        "narrator": "Jabir ibn Abdullah",
        "topics": ["justice", "oppression", "judgment day", "darkness"]
    },
    # FASTING
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 30, Hadith 1",
        "text": "The Prophet (ﷺ) said: 'Islam is based on five pillars: testifying that there is no god but Allah and that Muhammad is His Messenger, establishing prayer, paying Zakat, fasting in Ramadan, and performing Hajj.'",
        "arabic": "بُنِيَ الْإِسْلَامُ عَلَى خَمْسٍ",
        "narrator": "Ibn Umar",
        "topics": ["fasting", "ramadan", "pillars", "islam", "prayer", "zakat", "hajj"]
    },
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 30, Hadith 9",
        "text": "The Prophet (ﷺ) said: 'Whoever fasts during Ramadan out of sincere faith and hoping to attain Allah's rewards, then all his past sins will be forgiven.'",
        "arabic": "مَنْ صَامَ رَمَضَانَ إِيمَانًا وَاحْتِسَابًا غُفِرَ لَهُ مَا تَقَدَّمَ مِنْ ذَنْبِهِ",
        "narrator": "Abu Huraira",
        "topics": ["fasting", "ramadan", "sins", "forgiveness", "faith", "reward"]
    },
    # GRATITUDE
    {
        "collection": "Sunan Abu Dawud",
        "reference": "Book 42, Hadith 4811",
        "text": "The Prophet (ﷺ) said: 'He who does not thank people, does not thank Allah.'",
        "arabic": "لَا يَشْكُرُ اللَّهَ مَنْ لَا يَشْكُرُ النَّاسَ",
        "narrator": "Abu Huraira",
        "topics": ["gratitude", "thankfulness", "Allah", "people"]
    },
    # ANGER
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 137",
        "text": "A man said to the Prophet (ﷺ): 'Advise me.' He said: 'Do not become angry.' The man asked repeatedly and the Prophet answered each time: 'Do not become angry.'",
        "arabic": "لَا تَغْضَبْ",
        "narrator": "Abu Huraira",
        "topics": ["anger", "advice", "character", "self-control"]
    },
    # GOOD CHARACTER
    {
        "collection": "Sunan Tirmidhi",
        "reference": "Book 27, Hadith 2003",
        "text": "The Prophet (ﷺ) said: 'The most perfect of the believers in faith is the one with the best character among them. And the best of you are those who are best to their women.'",
        "arabic": "أَكْمَلُ الْمُؤْمِنِينَ إِيمَانًا أَحْسَنُهُمْ خُلُقًا",
        "narrator": "Abu Huraira",
        "topics": ["character", "faith", "women", "perfection", "believer"]
    },
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 59",
        "text": "The Prophet (ﷺ) said: 'The best among you are those who have the best manners and character.'",
        "arabic": "إِنَّ مِنْ خِيَارِكُمْ أَحْسَنَكُمْ أَخْلَاقًا",
        "narrator": "Abdullah ibn Amr",
        "topics": ["character", "manners", "best", "conduct"]
    },
    # DEATH & AFTERLIFE  
    {
        "collection": "Sunan Tirmidhi",
        "reference": "Book 36, Hadith 2459",
        "text": "The Prophet (ﷺ) said: 'Be in this world as if you were a stranger or a traveller along a path.'",
        "arabic": "كُنْ فِي الدُّنْيَا كَأَنَّكَ غَرِيبٌ أَوْ عَابِرُ سَبِيلٍ",
        "narrator": "Ibn Umar",
        "topics": ["death", "afterlife", "world", "dunya", "perspective"]
    },
    # BROTHERHOOD
    {
        "collection": "Sahih Bukhari",
        "reference": "Book 73, Hadith 70",
        "text": "The Prophet (ﷺ) said: 'None of you will have faith till he wishes for his brother what he likes for himself.'",
        "arabic": "لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ",
        "narrator": "Anas ibn Malik",
        "topics": ["brotherhood", "faith", "love", "believer", "unity"]
    },
]
