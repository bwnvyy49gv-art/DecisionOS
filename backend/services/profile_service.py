from models.user_profile import UserProfile


class ProfileService:

    def create_profile(self):
        return UserProfile()

    def update_goal(self, profile, goal):
        profile.career_goal = goal

    def add_skill(self, profile, skill):
        if skill not in profile.skills:
            profile.skills.append(skill)

    def add_interest(self, profile, interest):
        if interest not in profile.interests:
            profile.interests.append(interest)