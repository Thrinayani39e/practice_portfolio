"""Static strings and configuration values used across the app."""

APP_NAME = "MLH Fellow"
APP_DESCRIPTION = "My Personal Portfolio"

# Each entry drives both the navbar rendering and the route's page title.
# 'key' must match the active_page value passed from the route.
NAV_LINKS = [
    {"label": "About",      "href": "/about",       "key": "about"},
    {"label": "Experience", "href": "/experience",  "key": "experience"},
    {"label": "Projects",   "href": "/projects",    "key": "projects"},
    {"label": "Timeline",    "href": "/timeline",    "key": "timeline"},
    {"label": "Hobbies",    "href": "/hobbies",     "key": "hobbies"},
]

PAGE_TITLES = {
    "home":       APP_NAME,
    "about":      "About",
    "experience": "Experience",
    "projects":   "Projects",
    "timeline":   "Timeline",
    "hobbies":    "Hobbies",
}

EDUCATION = [
    {
        "degree": "MS, Computer Science and Software Engineering",
        "school": "University of Washington, Bothell",
        "location": "Bothell, WA",
        "status": "Expected March 2027 · GPA: 3.83/4.0",
    },
]

EXPERIENCES = [
    {
        "role": "Software Engineer Intern",
        "company": "Ravenna – Seattle, WA",
        "dates": "Jul 2026 – Present",
        "logo": "img/experience/ravenna.png",
        "current": True,
        "bullets": [
            "Build and test OAuth-based integrations with third-party platforms; configure provider auth flows for new integration partners.",
            "Harden Ravenna's Foundry agentic codegen pipeline for automated TypeScript integration-function generation, debugging and resolving data-extraction failures across partner APIs.",
            "Flagged a data-retention gap in unbounded test-run execution logs and owned the fix end-to-end, implementing a 3-day
TTL sweep as a background job on the team’s BullMQ scheduler",
        ],
    },
    {
        "role": "Software Design Engineer",
        "company": "Schneider Electric – R&D, Industrial Automation",
        "dates": "Feb 2025 – Aug 2025",
        "logo": "img/experience/schneider.png",
        "current": False,
        "bullets": [
            "Reduced PLC license validation time by 30% by engineering a GSE mechanism for Unity M580 industrial controllers using C# and WPF with full unit test coverage, directly supporting factory automation workflows.",
            "Decreased carbon emission reporting latency for manufacturing plants by architecting a real-time edge computing pipeline using Python and FastAPI, improving operational visibility into production metrics.",
            "Accelerated vulnerability inspection workflows by building user management dashboards and RBAC-based access controls using Angular and ASP.NET.",
        ],
    },
    {
        "role": "Graduate Engineer Trainee",
        "company": "Schneider Electric – R&D, Industrial Automation",
        "dates": "Aug 2024 – Feb 2025",
        "logo": "img/experience/schneider.png",
        "current": False,
        "bullets": [
            "Reduced application load times by 20% by refactoring .NET, WPF, and Angular codebases supporting industrial automation software, with maintained unit test coverage across all modules.",
            "Accelerated database query execution by 40% by designing an ORM-based data architecture using SQLite and SQLAlchemy.",
        ],
    },
    {
        "role": "Application Engineer Intern",
        "company": "Schneider Electric – R&D, Industrial Automation",
        "dates": "Jan 2024 – Jul 2024",
        "logo": "img/experience/schneider.png",
        "current": False,
        "bullets": [
            "Shipped production-ready RBAC system using C#, Angular, and .NET with zero vulnerabilities across Sonar and Coverity static analysis; delivered clean, well-tested code reviewed by senior engineers.",
        ],
    },
    {
        "role": "Research Scholar",
        "company": "Amrita Vishwavidyapeetham",
        "dates": "Sep 2023 – Dec 2023",
        "logo": "img/experience/amrita.jpg",
        "current": False,
        "bullets": [
            "Worked under Dr. Rimjhim Padam Singh as a research scholar and published a work on leveraging Spiking Neural Networks for fashion dataset classification — IEEE, 2024.",
        ],
    },
    {
        "role": "Research Scholar",
        "company": "Amrita Vishwavidyapeetham",
        "dates": "Apr 2023 – Jun 2023",
        "logo": "img/experience/amrita.jpg",
        "current": False,
        "bullets": [
            "Worked under Dr. Jyotsna C. as a research scholar and published a work on CNN-based neural networks for age estimation with diverse facial datasets — IEEE, 2024.",
        ],
    },
]

HOBBIES = [
    {
        "name": "Painting and Art",
        "description": "My go-to stress reliever and 'touch some grass' activity — painting and art help me decompress and reset.",
        "image": "img/hobbies/thrinayani/art.jpeg",
    },
    {
        "name": "Cafe Hopping",
        "description": "I love trying new coffee varieties and different cuisines — there's always a new spot to explore!",
        "image": "img/hobbies/thrinayani/cafe.jpeg",
    },
]

PROJECTS = [
    {
        "name": "Fast Marching Method — Ride the Wave",
        "description": "Outperformed OpenCV's GraphCutSeamFinder and DPSeamFinder by implementing an FMM-based seam finder for optimal image seamlines. Solved the Eikonal equation over fused cost fields (color, edge, texture, saliency) for globally optimal seam paths.",
        "image": "img/projects/thrinayani/fmm.png",
        "link": "https://github.com/Thrinayani39e/Fast_Marching_Method_Ride_the_Wave",
    },
    {
        "name": "Distributed Rate Limiter Microservice",
        "description": "Production-ready distributed rate-limiting backend implementing token bucket and sliding window algorithms via Redis. Full audit trail persisted to PostgreSQL, HTTP 429 enforcement with per-client analytics, and deployed via Docker Swarm with GitHub Actions CI/CD.",
        "image": "img/projects/thrinayani/ratelimiter.png",
        "link": "https://github.com/Thrinayani39e/rate-limiter-service",
    },
]
