import sys
from detector import detect_environment
from skills import skills
from executor import run_command

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py run_tests")
        return

    skill_name = sys.argv[1]

    if skill_name not in skills:
        print("Skill not found")
        return

    env = detect_environment()
    print("Environment:", env)

    skill = skills[skill_name]

    if env == "host":
        command = skill["host_command"]
    else:
        command = skill["breeze_command"]

    success = run_command(command)

    # fallback
    if not success and env == "host":
        print("Trying fallback...")
        run_command(skill["breeze_command"])

if __name__ == "__main__":
    main()
