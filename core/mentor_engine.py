from core.composer_profile import ComposerProfile


class MentorEngine:

    def review_profile(self, profile: ComposerProfile):

        profile.recommendations.clear()

        profile.strengths.clear()

        profile.weaknesses.clear()

        # =====================================

        if profile.average_score >= 98:

            profile.strengths.append(

                "Exceptional musical consistency."

            )

        elif profile.average_score >= 95:

            profile.strengths.append(

                "Very stable composition quality."

            )

        else:

            profile.weaknesses.append(

                "Average score can still improve."

            )

        # =====================================

        if profile.average_emotion >= 95:

            profile.strengths.append(

                "Excellent emotional writing."

            )

        if profile.average_originality >= 95:

            profile.strengths.append(

                "Strong originality."

            )

        if profile.average_commercial < 90:

            profile.weaknesses.append(

                "Commercial potential could be improved."

            )

        # =====================================

        if profile.favourite_genre:

            profile.recommendations.append(

                f"Continue exploring {profile.favourite_genre}."

            )

        if profile.favourite_lead:

            profile.recommendations.append(

                f"Develop your signature sound with {profile.favourite_lead}."

            )

        if profile.average_suno < 95:

            profile.recommendations.append(

                "Optimize prompts for Suno compatibility."

            )

        if profile.total_tracks > 500:

            profile.recommendations.append(

                "You have enough material to build a professional album."

            )

        if profile.total_tracks > 2000:

            profile.recommendations.append(

                "Your musical identity is becoming recognizable."

            )

        return profile

    # =====================================

    def speak(self, profile: ComposerProfile):

        text = []

        text.append(

            f"You have created {profile.total_tracks} tracks."

        )

        text.append(

            f"Average AI Score is {profile.average_score}."

        )

        if profile.favourite_genre:

            text.append(

                f"Your strongest genre is {profile.favourite_genre}."

            )

        if profile.favourite_lead:

            text.append(

                f"Your signature instrument is {profile.favourite_lead}."

            )

        if profile.recommendations:

            text.append("")

            text.append("My advice:")

            for tip in profile.recommendations:

                text.append(

                    f"• {tip}"

                )

        return "\n".join(text)


mentor_engine = MentorEngine()