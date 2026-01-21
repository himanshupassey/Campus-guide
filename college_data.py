# college_data.py

college_info = { 
    "ITS_Ghaziabad": { 
        "basic": { "name": "Institute of Technology & Science (ITS)", "location": "Ghaziabad, Uttar Pradesh, India", "website": "https://www.its.edu.in/", "email": "admissions@its.edu.in", "phone": "18001800840" }, 
        "courses": { 
            "btech": { "full_name": "Bachelor of Technology", "duration": "4 Years", "eligibility": "10+2 with PCM and required entrance", "fees": "₹8,00,000 - ₹12,00,000", "description": "Engineering degree with multiple branches" }, 
            "bca": { "full_name": "Bachelor of Computer Applications", "duration": "3 Years", "eligibility": "50% in 10+2", "fees": "₹4,94,000", "description": "Undergraduate in computer applications" }, 
            "bba": { "full_name": "Bachelor of Business Administration", "duration": "3 Years", "eligibility": "50% in 10+2", "fees": "₹4,94,000", "description": "Undergraduate business program" }, 
            "mba": { "full_name": "Master of Business Administration", "duration": "2 Years", "eligibility": "Graduation + entrance", "fees": "₹6,00,000 - ₹8,00,000", "description": "Postgraduate management degree" } 
        }, 
        "faculty": [ "Dr. Ashok Kumar", "Dr. Seema Singh", "Mr. Rahul Verma" ], 
        "library": { "books": "40,000+", "digital_access": "Online Public Access Catalogue", "seating_capacity": "200+" }, 
        "sports": [ "Cricket", "Basketball", "Badminton", "Volleyball", "Chess" ], 
        "placements": { "assistance": "100% placement support", "companies": [ "TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Amazon", "Deloitte" ], "average_package": "₹3,00,000 - ₹6,00,000" } 
    }, 
    "Amity_University_Noida": { 
        "basic": { "name": "Amity University, Noida", "location": "Sector-125, Noida, Uttar Pradesh, India", "website": "https://www.amity.edu/", "email": "info@amity.edu", "phone": "0120-4392398" }, 
        "courses": { 
            "btech": { "full_name": "Bachelor of Technology", "duration": "4 Years", "eligibility": "10+2 + JEE/CUET", "fees": "₹6,00,000 - ₹26,00,000 total", "description": "Engineering with multiple specializations" }, 
            "mba": { "full_name": "Master of Business Administration", "duration": "2 Years", "eligibility": "Graduation + CAT/XAT/MAT/CMAT", "fees": "₹6,50,000 - ₹8,00,000 per total", "description": "Management degree" }, 
            "bba": { "full_name": "Bachelor of Business Administration", "duration": "3 Years", "eligibility": "10+2", "fees": "₹3,00,000 - ₹3,50,000 per year", "description": "UG business degree" }, 
            "bca": { "full_name": "Bachelor of Computer Applications", "duration": "3 Years", "eligibility": "10+2", "fees": "₹6,42,000 total approx", "description": "Computer applications degree" }, 
            "bcom": { "full_name": "Bachelor of Commerce", "duration": "3 Years", "eligibility": "10+2", "fees": "₹2,84,000 - ₹4,40,000", "description": "Commerce UG" } 
        }, 
        "faculty": [ "Dr. Durgesh Kumar Tripathi", "Dr. Saikat Dutta", "Prof. Ajit Varma" ], 
        "library": { "books": "100,000+", "digital_access": "true", "seating_capacity": "500+" }, 
        "sports": [ "Football", "Tennis", "Swimming", "Athletics", "Basketball" ], 
        "placements": { "assistance": "Dedicated placement cell", "companies": [ "Adobe", "Flipkart", "Airtel", "Infosys" ], "average_package": "₹5,00,000 - ₹8,00,000" } 
    }, 
    "Chandigarh_University": { 
        "basic": { "name": "Chandigarh University (CU)", "location": "NH-95 Chandigarh-Ludhiana Highway, Mohali, Punjab, India", "website": "https://www.cuchd.in/", "email": "admissions@cumail.in", "phone": "1800121288800" }, 
        "courses": { 
            "btech": { "full_name": "Bachelor of Technology", "duration": "4 Years", "eligibility": "10+2 with CUCET/CBSE", "fees": "₹5,10,000 - ₹12,70,000 total", "description": "Engineering with many specializations" }, 
            "mba": { "full_name": "Master of Business Administration", "duration": "2 Years", "eligibility": "Graduation + CUCET/CUET PG", "fees": "₹5,12,000 - ₹7,94,000 total", "description": "Management programs" }, 
            "bsc": { "full_name": "Bachelor of Science", "duration": "3 Years", "eligibility": "10+2", "fees": "₹3,40,000 - ₹8,60,000", "description": "UG science" }, 
            "bca": { "full_name": "Bachelor of Computer Applications", "duration": "3 Years", "eligibility": "10+2", "fees": "₹86,500 - ₹89,500 per semester", "description": "Computer application degree" } 
        }, 
        "faculty": [ "Prof. Rajeev Sharma", "Dr. Anupama Sinha", "Mr. Vijay Verma" ], 
        "library": { "books": "80,000+", "digital_access": "true", "seating_capacity": "400+" }, 
        "sports": [ "Cricket", "Football", "Basketball", "Chess" ], 
        "placements": { "assistance": "Active placement cell", "companies": [ "Infosys", "Cognizant", "Amazon", "Deloitte" ], "average_package": "₹4,00,000 - ₹7,00,000" } 
    }, 
    "BITS_Pilani": { 
        "basic": { "name": "Birla Institute of Technology and Science, Pilani (BITS)", "location": "Pilani, Rajasthan, India", "website": "https://www.bits-pilani.ac.in/", "email": "admission@pilani.bits-pilani.ac.in", "phone": "+91-1596-xxx-xxxx" }, 
        "courses": { 
            "btech": { "full_name": "Bachelor of Engineering / Technology", "duration": "4 Years", "eligibility": "BITSAT", "fees": "₹19,00,000 - ₹22,00,000 total", "description": "Premier engineering degree" }, 
            "mtech": { "full_name": "Master of Technology / Engineering", "duration": "2 Years", "eligibility": "GATE/BITS HD", "fees": "₹2,42,000 - ₹10,40,000 total", "description": "Postgraduate engineering" }, 
            "mba": { "full_name": "Master of Business Administration", "duration": "2 Years", "eligibility": "GMAT/CAT", "fees": "₹8,00,000 - ₹12,00,000 approx", "description": "Management program" } 
        }, 
        "faculty": [ "Dr. S. Balasubramaniam", "Prof. Meera Nair", "Dr. Rajeev Gupta" ], 
        "library": { "books": "150,000+", "digital_access": "true", "seating_capacity": "600+" }, 
        "sports": [ "Cricket", "Tennis", "Basketball", "Badminton" ], 
        "placements": { "assistance": "Strong placement record", "companies": [ "Google", "Microsoft", "Goldman Sachs", "Amazon" ], "average_package": "₹18,00,000 - ₹22,00,000" } 
    }, 
    "Delhi_University": { 
        "basic": { "name": "University of Delhi (DU)", "location": "Delhi, India", "website": "https://www.du.ac.in/", "email": "info@du.ac.in", "phone": "+91-11-27667700" }, 
        "courses": { 
            "ba": { "full_name": "Bachelor of Arts (Honours)", "duration": "3 Years", "eligibility": "10+2 + CUET", "fees": "₹20,000 - ₹75,000 total approx", "description": "Undergraduate arts" }, 
            "bsc": { "full_name": "Bachelor of Science", "duration": "3 Years", "eligibility": "10+2 + CUET", "fees": "₹20,000 - ₹80,000 total approx", "description": "Undergraduate science" }, 
            "bcom": { "full_name": "Bachelor of Commerce", "duration": "3 Years", "eligibility": "10+2 + CUET", "fees": "₹20,000 - ₹70,000 total approx", "description": "Undergraduate commerce" }, 
            "mba": { "full_name": "Master of Business Administration", "duration": "2 Years", "eligibility": "Graduation + CAT/CUET PG", "fees": "₹50,000 - ₹60,000 per year approx", "description": "Postgraduate management" } 
        }, 
        "faculty": [ "Dr. Anil Sahasrabudhe", "Prof. Shobha Bagai", "Dr. Pankaj Garg" ], 
        "library": { "books": "200,000+", "digital_access": "true", "seating_capacity": "1000+" }, 
        "sports": [ "Football", "Cricket", "Athletics", "Badminton" ], 
        "placements": { "assistance": "Varies by college", "companies": [ "Accenture", "KPMG", "EY", "Kotak" ], "average_package": "₹5,00,000 - ₹12,00,000" } 
    }, 
    "Indraprastha_University": { 
        "basic": { "name": "Guru Gobind Singh Indraprastha University (IPU)", "location": "Delhi, India", "website": "https://www.ipu.ac.in/", "email": "info@ipu.ac.in", "phone": "+91-11-xxxx-xxxx" }, 
        "courses": { 
            "btech": { "full_name": "Bachelor of Technology", "duration": "4 Years", "eligibility": "10+2 + CET/entrance", "fees": "₹5,60,000 total approx", "description": "Engineering degree" }, 
            "bba": { "full_name": "Bachelor of Business Administration", "duration": "3 Years", "eligibility": "10+2 + CET", "fees": "₹2,50,000 - ₹3,00,000 total", "description": "Management UG" }, 
            "bca": { "full_name": "Bachelor of Computer Applications", "duration": "3 Years", "eligibility": "10+2 + CET", "fees": "₹2,25,000 - ₹2,75,000 total", "description": "Computer applications UG" }, 
            "mba": { "full_name": "Master of Business Administration", "duration": "2 Years", "eligibility": "Graduation + CET/entrance", "fees": "₹4,00,000 - ₹6,00,000 total", "description": "Management PG" } 
        }, 
        "faculty": [ "Dr. Rajeev Bhatia", "Prof. Meena Sharma", "Dr. Amit Singh" ], 
        "library": { "books": "80,000+", "digital_access": "true", "seating_capacity": "500+" }, 
        "sports": [ "Volleyball", "Basketball", "Cricket", "Athletics" ], 
        "placements": { "assistance": "University and affiliated colleges", "companies": [ "TCS", "Capgemini", "Infosys", "Amazon" ], "average_package": "₹4,00,000 - ₹8,00,000" } 
    } 
}

def chatbot_logic(user_msg):
    msg = user_msg.lower().strip()

    # ---------- 1. SMALL TALK / GREETINGS ----------
    if msg in ["hi", "hello", "hey", "hii", "help"]:
        return (
            "Hi 👋 I can help you with:\n"
            "• Courses & Fees\n"
            "• Placements & Recruiters\n"
            "• Sports & Faculty\n\n"
            "Try asking: 'BCA fees at Amity' or 'BITS placements'"
        )

    if msg in ["thanks", "thank you", "thx", "okay thanks", "ok thanks"]:
        return "You're very welcome! 😊 Is there anything else I can help you with?"

    if msg in ["bye", "goodbye", "ok bye", "exit", "okay"]:
        return "Goodbye! 👋 Have a great day and good luck with your college search!"

    if msg in ["ok", "okay", "fine", "understood"]:
        return "Great! Let me know if you have any other questions."
    
    if msg in ["who", "who are you", "what is your name", "what do you do", "who are you?"]:
        return "I am the Campus Guide Bot 🤖. I help students find information about colleges, courses, and fees quickly!"

    # ---------- 2. NEGATIVE / CLOSING (NEW FIX) ----------
    # This prevents "no", "nope", "nothing" from being logged as errors
    if msg in ["no", "nope", "nah", "no thanks", "nothing", "not really"]:
        return "Alright! Feel free to ask if you need anything else later. 👋"

    # ---------- 3. DETECT COLLEGE ----------
    college = None
    if "its" in msg:
        college = "ITS_Ghaziabad"
    elif "amity" in msg:
        college = "Amity_University_Noida"
    elif "chandigarh" in msg or "cu" in msg:
        college = "Chandigarh_University"
    elif "bits" in msg:
        college = "BITS_Pilani"
    elif "du" in msg or "delhi university" in msg:
        college = "Delhi_University"
    elif "ipu" in msg or "indraprastha" in msg:
        college = "Indraprastha_University"

    # If NO college found, check if they asked a specific keyword without a college
    if not college:
        if any(word in msg for word in ["fee", "course", "placement", "sports", "faculty"]):
            return "Which college are you interested in? (e.g., Amity, ITS, DU, BITS, IPU, or Chandigarh University)"
        
        # Log purely unknown queries
        return "UNANSWERED_QUERY"

    data = college_info[college]

    # ---------- 4. DETECT COURSE ----------
    course = None
    for c in data["courses"].keys():
        if c in msg:
            course = c
            break

    # ---------- 5. SPECIFIC QUERIES ----------
    # FEES
    if "fee" in msg or "cost" in msg or "price" in msg:
        if course:
            course_data = data["courses"][course]
            return (
                f"💰 {course_data['full_name']} at {data['basic']['name']}\n"
                f"• Duration: {course_data['duration']}\n"
                f"• Fees: {course_data['fees']}"
            )
        else:
            return (
                f"Please specify the course. Available courses at {data['basic']['name']}:\n"
                + ", ".join([v["full_name"] for v in data["courses"].values()])
            )

    # COURSES
    if "course" in msg or "study" in msg or "program" in msg:
        return f"📚 Courses offered at {data['basic']['name']}:\n" + "\n".join(
            [f"• {v['full_name']}" for v in data["courses"].values()]
        )

    # SPORTS
    if "sport" in msg or "game" in msg or "activity" in msg:
        return f"🏀 Sports at {data['basic']['name']}: " + ", ".join(data["sports"])

    # FACULTY
    if "faculty" in msg or "teacher" in msg or "professor" in msg:
        return f"👨‍🏫 Faculty members at {data['basic']['name']}:\n" + "\n".join([f"• {f}" for f in data["faculty"]])

    # PLACEMENTS
    if "placement" in msg or "job" in msg or "package" in msg or "recruiter" in msg:
        return (
            f"🎓 Placement Info for {data['basic']['name']}:\n"
            f"• Support: {data['placements']['assistance']}\n"
            f"• Top Recruiters: {', '.join(data['placements']['companies'])}\n"
            f"• Average Package: {data['placements']['average_package']}"
        )

    # ---------- 6. DEFAULT INFO ----------
    return (
        f"🏫 {data['basic']['name']}\n"
        f"📍 Location: {data['basic']['location']}\n"
        f"🌐 Website: {data['basic']['website']}\n"
        f"📞 Contact: {data['basic']['phone']}"
    )