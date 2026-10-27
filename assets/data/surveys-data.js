/**
 * PPRI Community Surveys Portal - Central Survey Definitions
 * 6 Active Surveys with 5 simple multiple-choice questions each.
 */
window.PPRI_SURVEYS = {
  "new-provinces": {
    id: "new-provinces",
    number: 1,
    title: "New Provinces & Local Representation",
    shortDescription: "Share your views on creating new provinces, regional representation and improving access to government.",
    detailedDescription: "Should Pakistan create new provinces, or focus on devolving power to local communities? Share your perspective on representation, administrative distance, and public services.",
    time: "3–5 minutes",
    icon: `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"></path><circle cx="12" cy="10" r="3"></circle></svg>`,
    questions: [
      {
        id: "q1",
        text: "Do you think Pakistan needs more provinces?",
        options: [
          "Yes",
          "No",
          "Maybe",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q2",
        text: "What do you think would be the biggest effect of creating new provinces?",
        options: [
          "Government offices could be closer to people",
          "Regions could have a stronger voice",
          "Public services could improve",
          "More administrative costs could be created",
          "It might not solve the main problems",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q3",
        text: "What is your biggest concern about creating new provinces?",
        options: [
          "The cost of setting up new governments",
          "Political disagreements",
          "Disputes over boundaries",
          "Whether public services would actually improve",
          "I do not have a major concern",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q4",
        text: "What should matter most when deciding the boundaries of a new province?",
        options: [
          "What people in the area want",
          "Distance from government offices",
          "Population size",
          "Local identity and culture",
          "Economic needs and available resources",
          "Existing district boundaries",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q5",
        text: "What should the government do first?",
        options: [
          "Study the costs and possible benefits",
          "Ask people in the affected areas",
          "Improve local government in existing provinces",
          "Study the option of creating more provinces",
          "Keep the present provincial structure",
          "Not sure",
          "Other (please specify)"
        ]
      }
    ]
  },

  "local-government": {
    id: "local-government",
    number: 2,
    title: "Stronger Local Government",
    shortDescription: "Tell us whether local governments need more power, funding and control over services in your area.",
    detailedDescription: "How effective is local government in your neighborhood? Share your experience with municipal services, local elections, and decision-making closer to citizens.",
    time: "3–5 minutes",
    icon: `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="10" width="18" height="11" rx="1"></rect><path d="M12 2l9 6H3l9-6z"></path><path d="M7 14v4"></path><path d="M12 14v4"></path><path d="M17 14v4"></path></svg>`,
    questions: [
      {
        id: "q1",
        text: "How easy is it to get help from your local government?",
        options: [
          "Very easy",
          "Somewhat easy",
          "Somewhat difficult",
          "Very difficult",
          "I have not used local government services",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q2",
        text: "Should local governments have more control over decisions affecting their areas?",
        options: [
          "Yes, much more control",
          "Yes, a little more control",
          "The current level is about right",
          "No, less control",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q3",
        text: "Which service should local government manage more directly?",
        options: [
          "Street repairs and local roads",
          "Waste collection and cleanliness",
          "Water supply and sanitation",
          "Local transport and traffic",
          "Parks and public spaces",
          "Local permits and building approvals",
          "Basic health or education services",
          "Other (please specify)"
        ]
      },
      {
        id: "q4",
        text: "What most often stops local government from solving local problems?",
        options: [
          "Not enough money",
          "Not enough decision-making power",
          "Not enough staff",
          "Delays in getting approval from higher offices",
          "Political interference",
          "Weak public oversight",
          "Not sure",
          "Other (please specify)"
        ]
      },
      {
        id: "q5",
        text: "What change would improve local government the most?",
        options: [
          "Regular local elections",
          "More reliable funding",
          "More control over staff and services",
          "Better ways for people to report problems",
          "Clear public reporting on spending and performance",
          "Not sure",
          "Other (please specify)"
        ]
      }
    ]
  },

  "government-delays": {
    id: "government-delays",
    number: 3,
    title: "Government Delays & Paperwork",
    shortDescription: "Tell us about delays, forms, waiting times and other problems when trying to use government services.",
    detailedDescription: "From identity documents to municipal permits, tell researchers about the waiting times, procedures, and practical barriers you face when dealing with public offices.",
    time: "3–5 minutes",
    icon: `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`,
    questions: [
      {
        id: "q1",
        text: "In the last 12 months, have you faced delays when using a government service?",
        options: [
          "Yes, more than once",
          "Yes, once",
          "No",
          "I have not used a government service during this period",
          "Other (please specify)"
        ]
      },
      {
        id: "q2",
        text: "Which type of service were you trying to use?",
        options: [
          "Identity documents or certificates",
          "Land or property work",
          "Business registration or a permit",
          "Local government or municipal services",
          "Health or education services",
          "Tax or payment-related services",
          "Court or legal services",
          "Other (please specify)"
        ]
      },
      {
        id: "q3",
        text: "What was the main problem?",
        options: [
          "Too many forms or documents",
          "Too many visits to the office",
          "Long waiting times",
          "Unclear instructions or requirements",
          "The responsible staff were unavailable",
          "Problems with an online system",
          "An unofficial payment was requested",
          "Other (please specify)"
        ]
      },
      {
        id: "q4",
        text: "How long did the process take?",
        options: [
          "The same day",
          "2–7 days",
          "1–4 weeks",
          "More than one month",
          "I am still waiting",
          "I did not face a delay",
          "Other (please specify)"
        ]
      },
      {
        id: "q5",
        text: "What would make government services easier to access?",
        options: [
          "Fewer documents and forms",
          "Clear instructions and official fees",
          "Fixed deadlines for completing work",
          "A single office for related services",
          "Online application tracking",
          "A better complaint system",
          "More local service offices",
          "Other (please specify)"
        ]
      }
    ]
  },

  "household-costs-inflation": {
    id: "household-costs-inflation",
    number: 4,
    title: "Household Costs & Inflation",
    shortDescription: "Share how rising prices affect your household budget and ability to pay for basic needs.",
    detailedDescription: "How are grocery prices, utility bills, and transport costs affecting family budgets? Share how your household manages expenses and what relief would help most.",
    time: "3–5 minutes",
    icon: `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>`,
    questions: [
      {
        id: "q1",
        text: "Over the last three months, how easy or difficult has it been to pay for your household's basic needs?",
        options: [
          "Very easy",
          "Somewhat easy",
          "Neither easy nor difficult",
          "Somewhat difficult",
          "Very difficult",
          "Prefer not to say",
          "Other (please specify)"
        ]
      },
      {
        id: "q2",
        text: "Which expense puts the most pressure on your household budget?",
        options: [
          "Food and groceries",
          "Electricity or gas bills",
          "Rent or housing costs",
          "Transport or fuel",
          "Health care and medicines",
          "Education and school costs",
          "Water and other utility bills",
          "Other (please specify)"
        ]
      },
      {
        id: "q3",
        text: "Compared with three months ago, how much money is left after paying for basic needs?",
        options: [
          "Much less",
          "A little less",
          "About the same",
          "More than before",
          "Not sure",
          "Prefer not to say",
          "Other (please specify)"
        ]
      },
      {
        id: "q4",
        text: "What have you had to do because of higher living costs?",
        options: [
          "Buy less or choose cheaper products",
          "Use savings",
          "Borrow money",
          "Delay paying bills",
          "Reduce travel",
          "Delay health care or education expenses",
          "Work extra hours or look for extra income",
          "Nothing has changed for me",
          "Prefer not to say",
          "Other (please specify)"
        ]
      },
      {
        id: "q5",
        text: "What would help your household the most?",
        options: [
          "More affordable food",
          "Lower electricity and gas bills",
          "Better pay or more income",
          "Financial support for households that need it",
          "Lower transport costs",
          "More affordable housing",
          "Lower health care or education costs",
          "Other (please specify)"
        ]
      }
    ]
  },

  "youth-jobs": {
    id: "youth-jobs",
    number: 5,
    title: "Youth Jobs & Career Opportunities",
    shortDescription: "Tell us about job opportunities, skills, pay and the challenges young people face when planning their future in Pakistan.",
    detailedDescription: "Whether you are a student, recent graduate, worker, or job seeker, share what barriers matter most in Pakistan's job market and what support is needed.",
    time: "3–5 minutes",
    icon: `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>`,
    questions: [
      {
        id: "q1",
        text: "Which option best describes your current situation?",
        options: [
          "Studying",
          "Working full-time",
          "Working part-time",
          "Looking for a job",
          "Self-employed or running a business",
          "Learning skills or completing training",
          "Not working or studying at present",
          "Other (please specify)"
        ]
      },
      {
        id: "q2",
        text: "What is the biggest challenge in finding a suitable job?",
        options: [
          "Not enough jobs available",
          "Employers want work experience",
          "I need more skills or training",
          "Pay is too low",
          "Suitable jobs are too far away",
          "I lack useful career contacts",
          "Hiring does not feel fair",
          "Other (please specify)"
        ]
      },
      {
        id: "q3",
        text: "What kind of support would help you the most?",
        options: [
          "Training linked to real job opportunities",
          "Paid internships or work experience",
          "Help with CVs and job interviews",
          "Help finding suitable jobs",
          "Digital skills or freelance-work training",
          "Support to start a small business",
          "Career advice and information",
          "Other (please specify)"
        ]
      },
      {
        id: "q4",
        text: "Would you move to another city in Pakistan for a suitable job?",
        options: [
          "Yes",
          "No",
          "Maybe",
          "It depends on the pay and living costs",
          "It depends on family responsibilities",
          "I already live away from my home area for work",
          "Other (please specify)"
        ]
      },
      {
        id: "q5",
        text: "What matters most when choosing a job?",
        options: [
          "Better pay",
          "Job security",
          "Career growth and learning",
          "Location and travel time",
          "A safe and respectful workplace",
          "Benefits such as leave or health coverage",
          "Flexible or remote work",
          "Other (please specify)"
        ]
      }
    ]
  },

  "jobs-abroad": {
    id: "jobs-abroad",
    number: 6,
    title: "Jobs Abroad & Moving for Work",
    shortDescription: "Share why people consider working abroad, what makes it difficult and what could help them find good work.",
    detailedDescription: "Share why Pakistani workers and professionals consider employment abroad, what obstacles exist around visas and recruitment, and what could encourage staying.",
    time: "3–5 minutes",
    icon: `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>`,
    questions: [
      {
        id: "q1",
        text: "Have you thought about moving abroad for work?",
        options: [
          "I am actively preparing to move",
          "I am seriously considering it",
          "I have thought about it but have not decided",
          "I am not considering it",
          "I already work abroad",
          "Other (please specify)"
        ]
      },
      {
        id: "q2",
        text: "What is the main reason you might want to work abroad?",
        options: [
          "Better pay",
          "More job opportunities",
          "Better career growth or skills",
          "A more stable future",
          "Family reasons",
          "Better opportunities in my field",
          "Other (please specify)"
        ]
      },
      {
        id: "q3",
        text: "What would be your biggest difficulty in finding work abroad?",
        options: [
          "Visa costs and paperwork",
          "The cost of travel or relocation",
          "Lack of required skills or language ability",
          "Lack of reliable information",
          "Concern about fake jobs or recruitment fraud",
          "Family responsibilities",
          "Not knowing where to find legitimate opportunities",
          "Other (please specify)"
        ]
      },
      {
        id: "q4",
        text: "What could make you more likely to stay and work in Pakistan?",
        options: [
          "Better pay",
          "More jobs matching my skills",
          "Fair hiring and promotion",
          "Safer and more stable work",
          "Support to start a business",
          "Better public services and living conditions",
          "I would still prefer to work abroad",
          "Other (please specify)"
        ]
      },
      {
        id: "q5",
        text: "What support would be most useful for people planning to work abroad legally?",
        options: [
          "Reliable information about jobs and visas",
          "Help finding verified employers or recruiters",
          "Affordable skills or language training",
          "Help preparing documents",
          "Information about worker rights and protections",
          "Support for people returning to Pakistan",
          "More suitable jobs in Pakistan",
          "Other (please specify)"
        ]
      }
    ]
  }
};
