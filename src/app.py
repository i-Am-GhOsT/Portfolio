from pathlib import Path
import streamlit as st
from PIL import Image
import os

# ----- PATH SETTINGS ----

curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cdw()
css_file = curr_dir / "styles" / "main.css"

# Resume Section
RESUME = "https://ugc.production.linktr.ee/5c226145-4213-4733-b41f-e1781f2b67ba_Arindam-Tanti-2024.pdf"
# RESUME = curr_dir / "assets" / "Resume.pdf"
# with open(RESUME, "rb") as RESUME_handle:
#     PDFByte = RESUME_handle.read()

# Profile Signature Sections
# If you want to have a photo as a sigiatal signature then,
# signature_file = curr_dir / "assets" / "Signature.png" # ENABLE, IF YOU WANT A PICTURE
SIGNATURE = "Arindam Tanti" # DISABLE, IF YOU WANT A PICTURE
#SIGNATURE = Image.open(signature_file)

# Profile Picture Section
# If you want to have a gif profile pic the portfolio, 
# then comment line with (profile-pic.gif) and uncomment line with (profile-pic.png).
PROFILE_PIC = curr_dir / "assets" / "profile-pic.png"
# PROFILE_PIC_GIF = curr_dir / "assets" / "profile-pic.gif"
PROFILE_PIC_file_handle = Image.open(PROFILE_PIC)


# -- GENERAL SETTINGS ---

PAGE_TITLE = "Portfolio | Arindam Tanti"
PAGE_ICON = ":wave:"
NAME = "Arindam Tanti"
DESCRIPTION = '''
🧙🏼‍♂️ Cloud SRE at [*VMware*](https://www.vmware.com) by [**Broadcom**](https://www.broadcom.com), [**Ex-Capgemini**](https://www.capgemini.com)
\n
VCP DCV | ☁️ Multi Cloud | 🛜 Networking | ♾️ DevOps | Distributed Systems, Data Center, Virtualization
🐳 Docker | ⚙️ Automation | 👀 Monitoring | 🏭 ITSM/ITIL
🔍 Triaging/Post-mortem | 👨🏻‍💻 Security Enthusiat'''
EMAIL = "arindamtanti123@gmail.com"
SOCIAL_MEDIA = {
    "Youtube": "https://www.youtube.com/channel/UCKivlgu2uoAxi-ChnAwUB-A",
    "LinkedIn": "https://www.linkedin.com/in/arindam-tanti/",
    "GitHub": "https://github.com/i-Am-GhOsT",
    "LinkTree": "https://linktr.ee/arindamtanti",
}

PROJECTS = {
    "🏆 Blogs by TuxTechLab": "https://tuxtechlab.github.io/Blogs/",
    "🏆 ChatBot Using Python": "",
    "🏆 Webcam Pulse Detection System": "https://drive.google.com/drive/u/1/folders/0B39LEvivQgQ1OUU0RkxVWVA2RFk?resourcekey=0-l39ttdjRpYveOZK3PRQyXw"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Portfolio")


# --- LOAD CSS, PDF, PROFILE PIC ---

with open(css_file) as style_file_handle:
    st.markdown(
        "<style>{}</style>".format(style_file_handle.read()), unsafe_allow_html=True
    )


# --- INTRO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(PROFILE_PIC_file_handle,clamp=False)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # Enable if you want to upload a PDF File into the repo.
    # st.download_button(
    #     label="**⬇️ Download Resumé**",
    #     data=PDFByte,
    #     file_name=RESUME.name,
    #     mime="application/octet-stream",
    # )
    # st.write("📬", EMAIL, unsafe_allow_html=False)
    st.link_button("**📄 Download Resumé**", RESUME)
    st.link_button("**📬 Mail Me**", "mailto:{}".format(EMAIL))
# --- SOCIAL LINKS ---

st.write("#")
st.subheader("Contact Me")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- ABOUT ---

st.write("#")
st.subheader("About Me 🙇‍♂️")
st.write(
    """
*Hi Everyone 👋😊*,

Meet a tech enthusiast with a passion for exploring the depths of Computer Science and Technology, particularly in the realm of devops, SDLC, OS, networking, automation, virtualization, security, scripting, ITIL/ITSM. From tinkering with operating systems to delving into log analysis and RCA, my journey led me to embrace DevOps and SRE roles. Let's navigate this tech-driven world together!
    """
)
col1, col2 = st.columns(2, gap="large")
with col2:
    st.write("*Warm Regards,*")
    st.write("Arindam Tanti")
    # st.image(SIGNATURE,clamp=False)

# --- WORK HISTORY ---
# Broadcom
st.write("#")
st.subheader("Work History")

col1, col2 = st.columns([0.1, 1])
with col1:
    st.image("https://seeklogo.com/images/B/broadcom-logo-7B264C2D56-seeklogo.com.png", width=38)

with col2:
    st.markdown("#### [**Broadcom**](https://www.broadcom.com)")

st.write("#### **Site Reliability Engineer**")
st.write(
    "*Nov 2023 - Present, 📍 [Bengaluru](https://maps.app.goo.gl/Rh8RqocqWceheSSs9) 🇮🇳 India*"
)
st.write(
    """
VMware is Acquired By Broadcom in Nov, 2023. Currently Part Of Broadcom GTO with similar responsibilities.
    """
)
st.write("---")
# VMware
col1, col2 = st.columns([0.1, 1])
with col1:
    st.image("https://www.vmware.com/content/dam/digitalmarketing/vmware/en/images/icons/vmw-avatar-corporate.png", width=38, clamp=False)

with col2:
    st.markdown("#### [**VMware**](https://www.vmware.com)")
st.write("#### **Site Reliability Engineer**")
st.write(
    "*June 2022 - Nov 2023, 📍 [Bengaluru](https://maps.app.goo.gl/Rh8RqocqWceheSSs9) 🇮🇳 India*"
)
st.write(
    """
Certified SDDC Professional with expertise in Virtualization, Operations and Trouble shooting SDDC infra and maintaining life cycle. Attending operation incidents. Federating a structural documented solutions with tools, app and culture. 

> **VCP DCV Certification➡️ https://rb.gy/7g06ab**

Working as full-time SRE for IaaS, PaaS on Cloud Operations for VMware Command Center.

- 👉 Being a SRE in VMware is like being a MARCOS. Dealing with real life, real time issues of a running Super High Reliable Distributed Systems and doing post-mortem of them. 
- 👉 Runbook validation for alerts.
- 👉 Attend Pager Duty escalations for policy based incident response. 
- 👉 Automation, ChatOps, GitOPs, Auto Remidiation, Auto validation
- 👉 Learning more about Virtualization, Operations and Site Reliability Strategies.
    """
)
st.write("---")
# Capgemini
col1, col2 = st.columns([0.1, 1])
with col1:
    st.image("https://banner2.cleanpng.com/20180401/wfe/kisspng-capgemini-sogeti-engineering-information-industry-blockchain-5ac0a0f85f2bd0.5897938315225735603898.jpg", width=50, clamp=False)

with col2:
    st.markdown("#### [**Capgemini**](https://www.Capgemini.com)")
st.write("#### **Associate Consultant**")
st.write(
    "*Mar 2021 - Jun 2022 | 📍 [Kolkata](https://maps.app.goo.gl/yuuRpTDN9NNGbz2v7), 🇮🇳 India*"
)
st.write(
    """
Worked As A full-time DevOps Engineer

- 👉 Maintain CI/CD Pipeline.
- 👉 Troubleshoot and Administrate Current Infrastructure.
- 👉 Build Code from Source & act as conjuntion between Dev & QA.
- 👉 Jenkins, Atlassian Stack, Jira, Bugzilla. 
- 👉 Report on Daily Automated Tasks' Statistics.
- 👉 Implement new ideas to in-corporate manual task to automation in currrent pipeline & infrastructure.
- 👉 Handle client side interactions with Dev and also part of client stand-up scrum.
- 👉 Worked on security vulnarabilities of products which have security flaws reported by customer or 3rd party researcher.
         """
)
st.write("#### **Senior Software Analyst**")
st.write("*Apr 2020 - Apr 2021 | Remote, 🇮🇳 India*")
st.write(
    """
Worked As A Developer on Storage Appliance and Open Source interoperable protocols (NFS, SMB, NDMP). 

Side-By-Side Worked As A DevOps Engineer

- 👉 Implementing automation in CI/CD pipeline to improve productivity in an Agile environment.
- 👉 Have good understanding on Jenkins and how to configure it with projects. 
- 👉 Deployed Code Review Server For Reviewing of Code changes done by developers in team.
- 👉 Worked on implementation of API and Web Apps to incorporate REST request form Web App to target Service.
- 👉 Voluntarily Contributed into brain stromed ideas and PoC concepts.
- 👉 Took ownership of CI/CD pipeline for 2 projects and maintaining the project infrastructure for the team.
- 👉 Implemented automated mail notification that helped to get instant updates of Jenkins Job of Several Projects.
         """
)
st.write("#### **Software Analyst**")
st.write(
    "*Feb 2019 - Apr 2020 | [Mumbai](https://maps.app.goo.gl/quP3w9fHGffHURt18), 🇮🇳 India*"
)
st.write(
    """
Worked as a developer in Storage, specifically Enterprise NAS Appliance FluidFS, SAN.

- 👉 Includes solving high serverity issues related to File Locks, File-system Panic, System Stuck as a dev team member.
- 👉 An active member to work on new-releases. Even Worked on Build Verification Test & Integration of ongoing fixes. 
- 👉 Favorite Topics: NFS/SMB locks, Stale Locks, FileHandle, Oplock/Range Lock, Samba, Quota, nlm locking, Debugging BVT stream
- 👉 Investigation on active reported bugs.

Learning good practices from the Agile-Scrum dev-environment.
         """
)

# --- SKILLS ---

st.write("#")
st.subheader("Skills")
st.write(
    """
- 👨‍💻 **Programming** 
    - *Backend:* C, C++, Python
    - *Frontend:* Html, CSS ( Tailwind, BootStrap )
    - *Scripting:*  Shell, Batch, Bash, Powershell
- 💻 **Operating System** 
    - *Windows:* Win8, 10, 11, 2012, 2016, 2019 Server falvours
    - *Linux:* Debian, Cent OS, Ubuntu, Alpine, Kali
    - *Macintosh*
    - *VMware* **ESXi**, **vCenter**, **Photos OS**
    - Exploring new Operating Systems based on requirements
- 📜 **Database** 
    - *RDBMS:* Oracle SQL, PostgresQL
    - *NoSQL:* MongoDB
- ⚙️ **CI/CD Tools**: 
    - *Automation:* Jenkins, Stack Storm, Ansible, Github Actions, GitOPs, vRealize Orchestration
    - *Project Management:* Jira, Kanban, Status Page, ChatOps, VMware Aria Suite
    - *Monitoring:* Uptime, CatchPoint, BlazeMeter, VMware Aria Logs
    - *SCM:* Git, Tortoise SVN, Perforce
    - *DSCM:* privately hosted in cloud, GitLab, GitHub
    - *Terminal:* zsh with custom plugins & theme, MobaXTerm, Tabby
    - *Containerization:* Docker, Vargrant
    - *Communications:* Twitter, Status Page, Slack/ MS-Teams/ E-Mail Notification, Scum/ weekly meeting
    - *Configration Management:* Ansible with Tower, Puppet
    - *Cloud* : Private Cloud, Multi cloud, AWS hands-on
- 🛜 Network, Protocols, Internet:
    - IPv4, Subnetting, Gateway, Bridge, Router
    - DNS, NTP, HTTPS, SSH, SSL on TCP, UDP
    - OSPF, BGP 
    - NFS, SMB, File system
    - Trusted, Demilitarized, Untrusted Tenants
    - Certificate Management, IAM, Active Directory Management, Access Control & Administration
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ Bachelor in Computer Science & Engineering
- ✅ Experienced in mangement level engament in ITIL/ ISTM operational works along with customer maangement.
- ✅ Experienced problem solver, belives in learning 1% daily. 
- ✅ Loves to collaborate and keep docuement of reproducable scenarios.
- ✅ Always eager to implement solutions for repititive tasks. A team player.
- ✅ Expertise in IaaS, PaaS, SaaS for production operation, support, incident resolutions.
- ✅ A delivery hero in solo tasks and a Machine Gun in collaborative tasks.
    """
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader(" Projects & Accomplishments ")
st.write("---")
for project, link in PROJECTS.items():
    st.write("[{}]({})".format(project, link))