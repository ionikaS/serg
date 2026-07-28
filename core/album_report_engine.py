from core.album_director import album_director


class AlbumReportEngine:

    def build(self, tracks):

        report = album_director.analyze(tracks)

        lines = []

        lines.append("========== AI ALBUM REPORT ==========")
        lines.append("")

        lines.append(f"Tracks : {report['track_count']}")
        lines.append("")

        # ==========================
        # Similarity
        # ==========================

        lines.append("SIMILAR TRACKS")

        if report["duplicates"]:

            for item in report["duplicates"]:

                lines.append(

                    f"Track {item['track1']} ↔ Track {item['track2']}"

                    f"   Similarity {item['similarity']}%"

                )

        else:

            lines.append("No similar tracks detected.")

        lines.append("")

        # ==========================
        # Flow
        # ==========================

        lines.append("ALBUM FLOW")

        for item in report["flow"]:

            lines.append(

                f"{item['from']} → {item['to']}"

                f"   {item['transition']}"

            )

        lines.append("")

        # ==========================
        # Energy
        # ==========================

        lines.append("ENERGY CURVE")

        for item in report["energy_curve"]:

            lines.append(

                f"Track {item['track']}"

                f"   {item['energy']}"

                f"   Score {item['score']}"

            )

        lines.append("")

        # ==========================
        # AI Recommendations
        # ==========================

        lines.append("AI RECOMMENDATIONS")

        for tip in report["recommendations"]:

            lines.append(f"• {tip}")

        return "\n".join(lines)


album_report_engine = AlbumReportEngine()