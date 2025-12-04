# ...existing code...
from pyscript import document  # type: ignore

clubs = {
    "Math Club": {
        "Name": "Math Club",
        "Description": "Math challenges and competitions.",
        "Meeting time": "Monday (2:30 PM - 4:30 PM)",
        "Location": "Room 404",
        "Club Moderator": "Mr. Gabuya",
        "Number of members": 16,
    },
    "SS": {
        "Name": "Social Studies Club",
        "Description": "Debates and social studies activities.",
        "Meeting time": "Tues & Thurs (3:00 - 4:00 PM)",
        "Location": "Room 409",
        "Club Moderator": "Mr. Roberto Lim",
        "Number of members": 21,
    },
    "Science": {
        "Name": "Science Club",
        "Description": "Experiments, fairs and projects.",
        "Meeting time": "Tue 3:00 PM / Fri 2:00 PM",
        "Location": "Lab A",
        "Club Moderator": "Ms. Maramag",
        "Number of members": 18,
    },
    "Band": {
        "Name": "Band Club",
        "Description": "Instrument practice and performances.",
        "Meeting time": "Mon–Wed (3:00 - 4:30 PM)",
        "Location": "Music Room",
        "Club Moderator": "Mr. Alumno",
        "Number of members": 42,
    },
    "Coms-Art": {
        "Name": "Coms Art Club",
        "Description": "Literature and arts activities.",
        "Meeting time": "Wed & Fri (3:00 - 4:00 PM)",
        "Location": "Room 406",
        "Club Moderator": "Ms. Fernandez",
        "Number of members": 23,
    },
    "VB": {
        "Name": "Volleyball Club",
        "Description": "Volleyball practice and tournaments.",
        "Meeting time": "Wednesday (3:00 - 5:00 PM)",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Ruiz",
        "Number of members": 24,
    },
}

def _ensure_output_div():
    out = document.getElementById("clubInfo")
    if out is None:
        wrapper = document.querySelector(".club-wrapper")
        if wrapper is None:
            wrapper = document.body
        out = document.createElement("div")
        out.id = "clubInfo"
        out.style.whiteSpace = "pre-wrap"
        out.style.marginTop = "12px"
        wrapper.appendChild(out)
    return out
    # ask copilot to give me a code and it gave me this to help me display it
def show_club_info(e=None):
    selected = document.getElementById("clubs").value
    info = clubs.get(selected)
    out = _ensure_output_div()

    if info:
        out.innerText = (
            f"Club Name: {info['Name']}\n"
            f"Description: {info['Description']}\n"
            f"Meeting time: {info['Meeting time']}\n"
            f"Location: {info['Location']}\n"
            f"Club Moderator: {info['Club Moderator']}\n"
            f"Number of members: {info['Number of members']}"
        )
    else:
        out.innerText = "Club information not found."

document.getElementById("showClub").addEventListener("click", show_club_info)
document.getElementById("clubs").addEventListener("change", show_club_info)

show_club_info()
