import unittest

import networkx as nx

from src.network_structure import VARIABLE_STATES, build_network


class TestNetworkStructure(unittest.TestCase):
    def test_network_has_exact_variables_and_states(self):
        network = build_network()

        self.assertEqual(set(network.nodes), set(VARIABLE_STATES))
        self.assertEqual(len(network.nodes), 10)
        self.assertEqual(
            VARIABLE_STATES,
            {
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
            },
        )

    def test_network_has_expected_edges_and_parents(self):
        network = build_network()

        expected_edges = {
            ("concept_1_difficulty", "concept_1_mastery"),
            ("concept_2_difficulty", "concept_2_mastery"),
            ("concept_3_difficulty", "concept_3_mastery"),
            ("concept_1_mastery", "exam_success"),
            ("concept_2_mastery", "exam_success"),
            ("concept_3_mastery", "exam_success"),
            ("stress_level", "exam_success"),
            ("exam_urgency", "exam_success"),
            ("study_action", "exam_success"),
        }
        self.assertEqual(set(network.edges), expected_edges)
        self.assertEqual(len(network.edges), 9)
        self.assertEqual(
            set(network.predecessors("exam_success")),
            {
                "concept_1_mastery",
                "concept_2_mastery",
                "concept_3_mastery",
                "stress_level",
                "exam_urgency",
                "study_action",
            },
        )
        self.assertEqual(
            set(network.predecessors("concept_1_mastery")),
            {"concept_1_difficulty"},
        )
        self.assertEqual(
            set(network.predecessors("concept_2_mastery")),
            {"concept_2_difficulty"},
        )
        self.assertEqual(
            set(network.predecessors("concept_3_mastery")),
            {"concept_3_difficulty"},
        )

    def test_network_is_acyclic_and_study_action_is_root(self):
        network = build_network()

        self.assertTrue(nx.is_directed_acyclic_graph(network))
        self.assertEqual(list(network.predecessors("study_action")), [])


if __name__ == "__main__":
    unittest.main()
