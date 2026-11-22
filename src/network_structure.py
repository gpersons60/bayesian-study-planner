from pgmpy.models import DiscreteBayesianNetwork


VARIABLE_STATES = {
    "concept_1_difficulty": ["easy", "hard"],
    "concept_2_difficulty": ["easy", "hard"],
    "concept_3_difficulty": ["easy", "hard"],
    "concept_1_mastery": ["low", "high"],
    "concept_2_mastery": ["low", "high"],
    "concept_3_mastery": ["low", "high"],
    "stress_level": ["low", "high"],
    "exam_urgency": ["far", "near"],
    "study_action": ["rest", "light", "moderate", "intense"],
    "exam_success": ["fail", "pass"],
}


def build_network() -> DiscreteBayesianNetwork:
    network = DiscreteBayesianNetwork(
        [
            ("concept_1_difficulty", "concept_1_mastery"),
            ("concept_2_difficulty", "concept_2_mastery"),
            ("concept_3_difficulty", "concept_3_mastery"),
            ("concept_1_mastery", "exam_success"),
            ("concept_2_mastery", "exam_success"),
            ("concept_3_mastery", "exam_success"),
            ("stress_level", "exam_success"),
            ("exam_urgency", "exam_success"),
            ("study_action", "exam_success"),
        ]
    )
    network.add_nodes_from(VARIABLE_STATES)
    return network
