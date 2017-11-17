from pprint import pprint
from dependencies import generate
from map import find_score, dictionary


def best_ans(question_deps, answer_list_deps):
    """Choose the best answer index, out of given answer list according to the question

    :type question_deps: dict
    :type answer_list_deps: list[dict]
    """
    scores = {}
    q_dependencies = list(generate(question_deps))

    for index, answer_deps in enumerate(answer_list_deps):
        a_dependencies = list(generate(answer_deps))

        # calculate scores
        scores[index + 1] = find_score(q_dependencies, a_dependencies)

    print 'Scores :'
    pprint(scores, indent=4)

    min_scores = min(scores.values())
    return [k for k, v in scores.iteritems() if v == min_scores]


def test():
    # Question - Can I use BPMN instead of BPEL via the Business Process profile?
    # Answers - The Business Process Profile supports both BPMN and BPEL.
    #           BPMN (activiti) database. BPS 3.5.0 introduces BPMN support by embedding popular Activiti BPMN engine
    q_deps = {u'corefs': {}, u'sentences': [{u'index': 0, u'enhancedDependencies': [{u'dep': u'ROOT', u'dependent': 3, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'use'}, {u'dep': u'aux', u'dependent': 1, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'Can'}, {u'dep': u'nsubj', u'dependent': 2, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'I'}, {u'dep': u'nsubj', u'dependent': 4, u'governorGloss': u'Process', u'governor': 11, u'dependentGloss': u'BPMN'}, {u'dep': u'case', u'dependent': 5, u'governorGloss': u'BPEL', u'governor': 7, u'dependentGloss': u'instead'}, {u'dep': u'mwe', u'dependent': 6, u'governorGloss': u'instead', u'governor': 5, u'dependentGloss': u'of'}, {u'dep': u'nmod:instead_of', u'dependent': 7, u'governorGloss': u'BPMN', u'governor': 4, u'dependentGloss': u'BPEL'}, {u'dep': u'case', u'dependent': 8, u'governorGloss': u'Business', u'governor': 10, u'dependentGloss': u'via'}, {u'dep': u'det', u'dependent': 9, u'governorGloss': u'Business', u'governor': 10, u'dependentGloss': u'the'}, {u'dep': u'nmod:via', u'dependent': 10, u'governorGloss': u'BPEL', u'governor': 7, u'dependentGloss': u'Business'}, {u'dep': u'ccomp', u'dependent': 11, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'Process'}, {u'dep': u'dobj', u'dependent': 12, u'governorGloss': u'Process', u'governor': 11, u'dependentGloss': u'profile'}, {u'dep': u'punct', u'dependent': 13, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'?'}], u'basicDependencies': [{u'dep': u'ROOT', u'dependent': 3, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'use'}, {u'dep': u'aux', u'dependent': 1, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'Can'}, {u'dep': u'nsubj', u'dependent': 2, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'I'}, {u'dep': u'nsubj', u'dependent': 4, u'governorGloss': u'Process', u'governor': 11, u'dependentGloss': u'BPMN'}, {u'dep': u'case', u'dependent': 5, u'governorGloss': u'BPEL', u'governor': 7, u'dependentGloss': u'instead'}, {u'dep': u'mwe', u'dependent': 6, u'governorGloss': u'instead', u'governor': 5, u'dependentGloss': u'of'}, {u'dep': u'nmod', u'dependent': 7, u'governorGloss': u'BPMN', u'governor': 4, u'dependentGloss': u'BPEL'}, {u'dep': u'case', u'dependent': 8, u'governorGloss': u'Business', u'governor': 10, u'dependentGloss': u'via'}, {u'dep': u'det', u'dependent': 9, u'governorGloss': u'Business', u'governor': 10, u'dependentGloss': u'the'}, {u'dep': u'nmod', u'dependent': 10, u'governorGloss': u'BPEL', u'governor': 7, u'dependentGloss': u'Business'}, {u'dep': u'ccomp', u'dependent': 11, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'Process'}, {u'dep': u'dobj', u'dependent': 12, u'governorGloss': u'Process', u'governor': 11, u'dependentGloss': u'profile'}, {u'dep': u'punct', u'dependent': 13, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'?'}], u'tokens': [{u'index': 1, u'word': u'Can', u'lemma': u'can', u'after': u' ', u'pos': u'MD', u'characterOffsetEnd': 3, u'speaker': u'PER0', u'characterOffsetBegin': 0, u'originalText': u'Can', u'ner': u'O', u'before': u''}, {u'index': 2, u'word': u'I', u'lemma': u'I', u'after': u' ', u'pos': u'PRP', u'characterOffsetEnd': 5, u'speaker': u'PER0', u'characterOffsetBegin': 4, u'originalText': u'I', u'ner': u'O', u'before': u' '}, {u'index': 3, u'word': u'use', u'lemma': u'use', u'after': u' ', u'pos': u'VB', u'characterOffsetEnd': 9, u'speaker': u'PER0', u'characterOffsetBegin': 6, u'originalText': u'use', u'ner': u'O', u'before': u' '}, {u'index': 4, u'word': u'BPMN', u'lemma': u'BPMN', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 14, u'speaker': u'PER0', u'characterOffsetBegin': 10, u'originalText': u'BPMN', u'ner': u'O', u'before': u' '}, {u'index': 5, u'word': u'instead', u'lemma': u'instead', u'after': u' ', u'pos': u'RB', u'characterOffsetEnd': 22, u'speaker': u'PER0', u'characterOffsetBegin': 15, u'originalText': u'instead', u'ner': u'O', u'before': u' '}, {u'index': 6, u'word': u'of', u'lemma': u'of', u'after': u' ', u'pos': u'IN', u'characterOffsetEnd': 25, u'speaker': u'PER0', u'characterOffsetBegin': 23, u'originalText': u'of', u'ner': u'O', u'before': u' '}, {u'index': 7, u'word': u'BPEL', u'lemma': u'BPEL', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 30, u'speaker': u'PER0', u'characterOffsetBegin': 26, u'originalText': u'BPEL', u'ner': u'O', u'before': u' '}, {u'index': 8, u'word': u'via', u'lemma': u'via', u'after': u' ', u'pos': u'IN', u'characterOffsetEnd': 34, u'speaker': u'PER0', u'characterOffsetBegin': 31, u'originalText': u'via', u'ner': u'O', u'before': u' '}, {u'index': 9, u'word': u'the', u'lemma': u'the', u'after': u' ', u'pos': u'DT', u'characterOffsetEnd': 38, u'speaker': u'PER0', u'characterOffsetBegin': 35, u'originalText': u'the', u'ner': u'O', u'before': u' '}, {u'index': 10, u'word': u'Business', u'lemma': u'business', u'after': u' ', u'pos': u'NN', u'characterOffsetEnd': 47, u'speaker': u'PER0', u'characterOffsetBegin': 39, u'originalText': u'Business', u'ner': u'O', u'before': u' '}, {u'index': 11, u'word': u'Process', u'lemma': u'process', u'after': u' ', u'pos': u'VB', u'characterOffsetEnd': 55, u'speaker': u'PER0', u'characterOffsetBegin': 48, u'originalText': u'Process', u'ner': u'O', u'before': u' '}, {u'index': 12, u'word': u'profile', u'lemma': u'profile', u'after': u'', u'pos': u'NN', u'characterOffsetEnd': 63, u'speaker': u'PER0', u'characterOffsetBegin': 56, u'originalText': u'profile', u'ner': u'O', u'before': u' '}, {u'index': 13, u'word': u'?', u'lemma': u'?', u'after': u'', u'pos': u'.', u'characterOffsetEnd': 64, u'speaker': u'PER0', u'characterOffsetBegin': 63, u'originalText': u'?', u'ner': u'O', u'before': u''}], u'parse': u'(ROOT\n  (SQ (MD Can)\n    (NP (PRP I))\n    (VP (VB use)\n      (S\n        (NP\n          (NP (NNP BPMN))\n          (PP (RB instead) (IN of)\n            (NP\n              (NP (NNP BPEL))\n              (PP (IN via)\n                (NP (DT the) (NN Business))))))\n        (VP (VB Process)\n          (NP (NN profile)))))\n    (. ?)))', u'enhancedPlusPlusDependencies': [{u'dep': u'ROOT', u'dependent': 3, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'use'}, {u'dep': u'aux', u'dependent': 1, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'Can'}, {u'dep': u'nsubj', u'dependent': 2, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'I'}, {u'dep': u'nsubj', u'dependent': 4, u'governorGloss': u'Process', u'governor': 11, u'dependentGloss': u'BPMN'}, {u'dep': u'case', u'dependent': 5, u'governorGloss': u'BPEL', u'governor': 7, u'dependentGloss': u'instead'}, {u'dep': u'mwe', u'dependent': 6, u'governorGloss': u'instead', u'governor': 5, u'dependentGloss': u'of'}, {u'dep': u'nmod:instead_of', u'dependent': 7, u'governorGloss': u'BPMN', u'governor': 4, u'dependentGloss': u'BPEL'}, {u'dep': u'case', u'dependent': 8, u'governorGloss': u'Business', u'governor': 10, u'dependentGloss': u'via'}, {u'dep': u'det', u'dependent': 9, u'governorGloss': u'Business', u'governor': 10, u'dependentGloss': u'the'}, {u'dep': u'nmod:via', u'dependent': 10, u'governorGloss': u'BPEL', u'governor': 7, u'dependentGloss': u'Business'}, {u'dep': u'ccomp', u'dependent': 11, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'Process'}, {u'dep': u'dobj', u'dependent': 12, u'governorGloss': u'Process', u'governor': 11, u'dependentGloss': u'profile'}, {u'dep': u'punct', u'dependent': 13, u'governorGloss': u'use', u'governor': 3, u'dependentGloss': u'?'}]}]}
    a_list_deps = [{u'corefs': {}, u'sentences': [{u'index': 0, u'enhancedDependencies': [{u'dep': u'ROOT', u'dependent': 5, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'supports'}, {u'dep': u'det', u'dependent': 1, u'governorGloss': u'Business', u'governor': 2, u'dependentGloss': u'The'}, {u'dep': u'nsubj', u'dependent': 2, u'governorGloss': u'Process', u'governor': 3, u'dependentGloss': u'Business'}, {u'dep': u'dep', u'dependent': 3, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'Process'}, {u'dep': u'dobj', u'dependent': 4, u'governorGloss': u'Process', u'governor': 3, u'dependentGloss': u'Profile'}, {u'dep': u'cc:preconj', u'dependent': 6, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'both'}, {u'dep': u'nsubj', u'dependent': 7, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'BPMN'}, {u'dep': u'cc', u'dependent': 8, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'and'}, {u'dep': u'nsubj', u'dependent': 9, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'BPEL.'}, {u'dep': u'conj:and', u'dependent': 9, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'BPEL.'}, {u'dep': u'punct', u'dependent': 10, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u','}, {u'dep': u'appos', u'dependent': 11, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'BPMN'}, {u'dep': u'punct', u'dependent': 12, u'governorGloss': u'activiti', u'governor': 13, u'dependentGloss': u'-LRB-'}, {u'dep': u'appos', u'dependent': 13, u'governorGloss': u'BPMN', u'governor': 11, u'dependentGloss': u'activiti'}, {u'dep': u'punct', u'dependent': 14, u'governorGloss': u'activiti', u'governor': 13, u'dependentGloss': u'-RRB-'}, {u'dep': u'dep', u'dependent': 15, u'governorGloss': u'BPMN', u'governor': 11, u'dependentGloss': u'database'}, {u'dep': u'punct', u'dependent': 16, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'.'}], u'basicDependencies': [{u'dep': u'ROOT', u'dependent': 5, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'supports'}, {u'dep': u'det', u'dependent': 1, u'governorGloss': u'Business', u'governor': 2, u'dependentGloss': u'The'}, {u'dep': u'nsubj', u'dependent': 2, u'governorGloss': u'Process', u'governor': 3, u'dependentGloss': u'Business'}, {u'dep': u'dep', u'dependent': 3, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'Process'}, {u'dep': u'dobj', u'dependent': 4, u'governorGloss': u'Process', u'governor': 3, u'dependentGloss': u'Profile'}, {u'dep': u'cc:preconj', u'dependent': 6, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'both'}, {u'dep': u'nsubj', u'dependent': 7, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'BPMN'}, {u'dep': u'cc', u'dependent': 8, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'and'}, {u'dep': u'conj', u'dependent': 9, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'BPEL.'}, {u'dep': u'punct', u'dependent': 10, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u','}, {u'dep': u'appos', u'dependent': 11, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'BPMN'}, {u'dep': u'punct', u'dependent': 12, u'governorGloss': u'activiti', u'governor': 13, u'dependentGloss': u'-LRB-'}, {u'dep': u'appos', u'dependent': 13, u'governorGloss': u'BPMN', u'governor': 11, u'dependentGloss': u'activiti'}, {u'dep': u'punct', u'dependent': 14, u'governorGloss': u'activiti', u'governor': 13, u'dependentGloss': u'-RRB-'}, {u'dep': u'dep', u'dependent': 15, u'governorGloss': u'BPMN', u'governor': 11, u'dependentGloss': u'database'}, {u'dep': u'punct', u'dependent': 16, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'.'}], u'tokens': [{u'index': 1, u'word': u'The', u'lemma': u'the', u'after': u' ', u'pos': u'DT', u'characterOffsetEnd': 3, u'speaker': u'PER0', u'characterOffsetBegin': 0, u'originalText': u'The', u'ner': u'O', u'before': u''}, {u'index': 2, u'word': u'Business', u'lemma': u'business', u'after': u' ', u'pos': u'NN', u'characterOffsetEnd': 12, u'speaker': u'PER0', u'characterOffsetBegin': 4, u'originalText': u'Business', u'ner': u'O', u'before': u' '}, {u'index': 3, u'word': u'Process', u'lemma': u'process', u'after': u' ', u'pos': u'VB', u'characterOffsetEnd': 20, u'speaker': u'PER0', u'characterOffsetBegin': 13, u'originalText': u'Process', u'ner': u'O', u'before': u' '}, {u'index': 4, u'word': u'Profile', u'lemma': u'Profile', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 28, u'speaker': u'PER0', u'characterOffsetBegin': 21, u'originalText': u'Profile', u'ner': u'O', u'before': u' '}, {u'index': 5, u'word': u'supports', u'lemma': u'support', u'after': u' ', u'pos': u'VBZ', u'characterOffsetEnd': 37, u'speaker': u'PER0', u'characterOffsetBegin': 29, u'originalText': u'supports', u'ner': u'O', u'before': u' '}, {u'index': 6, u'word': u'both', u'lemma': u'both', u'after': u' ', u'pos': u'DT', u'characterOffsetEnd': 42, u'speaker': u'PER0', u'characterOffsetBegin': 38, u'originalText': u'both', u'ner': u'O', u'before': u' '}, {u'index': 7, u'word': u'BPMN', u'lemma': u'bpmn', u'after': u' ', u'pos': u'NN', u'characterOffsetEnd': 47, u'speaker': u'PER0', u'characterOffsetBegin': 43, u'originalText': u'BPMN', u'ner': u'O', u'before': u' '}, {u'index': 8, u'word': u'and', u'lemma': u'and', u'after': u' ', u'pos': u'CC', u'characterOffsetEnd': 51, u'speaker': u'PER0', u'characterOffsetBegin': 48, u'originalText': u'and', u'ner': u'O', u'before': u' '}, {u'index': 9, u'word': u'BPEL.', u'lemma': u'bpel.', u'after': u'', u'pos': u'NN', u'characterOffsetEnd': 57, u'speaker': u'PER0', u'characterOffsetBegin': 52, u'originalText': u'BPEL.', u'ner': u'O', u'before': u' '}, {u'index': 10, u'word': u',', u'lemma': u',', u'after': u' ', u'pos': u',', u'characterOffsetEnd': 58, u'speaker': u'PER0', u'characterOffsetBegin': 57, u'originalText': u',', u'ner': u'O', u'before': u''}, {u'index': 11, u'word': u'BPMN', u'lemma': u'bpmn', u'after': u' ', u'pos': u'NN', u'characterOffsetEnd': 63, u'speaker': u'PER0', u'characterOffsetBegin': 59, u'originalText': u'BPMN', u'ner': u'O', u'before': u' '}, {u'index': 12, u'word': u'-LRB-', u'lemma': u'-lrb-', u'after': u'', u'pos': u'-LRB-', u'characterOffsetEnd': 65, u'speaker': u'PER0', u'characterOffsetBegin': 64, u'originalText': u'(', u'ner': u'O', u'before': u' '}, {u'index': 13, u'word': u'activiti', u'lemma': u'activiti', u'after': u'', u'pos': u'NN', u'characterOffsetEnd': 73, u'speaker': u'PER0', u'characterOffsetBegin': 65, u'originalText': u'activiti', u'ner': u'O', u'before': u''}, {u'index': 14, u'word': u'-RRB-', u'lemma': u'-rrb-', u'after': u' ', u'pos': u'-RRB-', u'characterOffsetEnd': 74, u'speaker': u'PER0', u'characterOffsetBegin': 73, u'originalText': u')', u'ner': u'O', u'before': u''}, {u'index': 15, u'word': u'database', u'lemma': u'database', u'after': u'', u'pos': u'NN', u'characterOffsetEnd': 83, u'speaker': u'PER0', u'characterOffsetBegin': 75, u'originalText': u'database', u'ner': u'O', u'before': u' '}, {u'index': 16, u'word': u'.', u'lemma': u'.', u'after': u' ', u'pos': u'.', u'characterOffsetEnd': 84, u'speaker': u'PER0', u'characterOffsetBegin': 83, u'originalText': u'.', u'ner': u'O', u'before': u''}], u'parse': u'(ROOT\n  (SINV\n    (S\n      (NP (DT The) (NN Business))\n      (VP (VB Process)\n        (NP (NNP Profile))))\n    (VP (VBZ supports))\n    (NP\n      (NP (DT both) (NN BPMN)\n        (CC and)\n        (NN BPEL.))\n      (, ,)\n      (NP\n        (NP (NN BPMN))\n        (PRN (-LRB- -LRB-)\n          (NP (NN activiti))\n          (-RRB- -RRB-))\n        (NP (NN database))))\n    (. .)))', u'enhancedPlusPlusDependencies': [{u'dep': u'ROOT', u'dependent': 5, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'supports'}, {u'dep': u'det', u'dependent': 1, u'governorGloss': u'Business', u'governor': 2, u'dependentGloss': u'The'}, {u'dep': u'nsubj', u'dependent': 2, u'governorGloss': u'Process', u'governor': 3, u'dependentGloss': u'Business'}, {u'dep': u'dep', u'dependent': 3, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'Process'}, {u'dep': u'dobj', u'dependent': 4, u'governorGloss': u'Process', u'governor': 3, u'dependentGloss': u'Profile'}, {u'dep': u'cc:preconj', u'dependent': 6, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'both'}, {u'dep': u'nsubj', u'dependent': 7, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'BPMN'}, {u'dep': u'cc', u'dependent': 8, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'and'}, {u'dep': u'nsubj', u'dependent': 9, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'BPEL.'}, {u'dep': u'conj:and', u'dependent': 9, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'BPEL.'}, {u'dep': u'punct', u'dependent': 10, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u','}, {u'dep': u'appos', u'dependent': 11, u'governorGloss': u'BPMN', u'governor': 7, u'dependentGloss': u'BPMN'}, {u'dep': u'punct', u'dependent': 12, u'governorGloss': u'activiti', u'governor': 13, u'dependentGloss': u'-LRB-'}, {u'dep': u'appos', u'dependent': 13, u'governorGloss': u'BPMN', u'governor': 11, u'dependentGloss': u'activiti'}, {u'dep': u'punct', u'dependent': 14, u'governorGloss': u'activiti', u'governor': 13, u'dependentGloss': u'-RRB-'}, {u'dep': u'dep', u'dependent': 15, u'governorGloss': u'BPMN', u'governor': 11, u'dependentGloss': u'database'}, {u'dep': u'punct', u'dependent': 16, u'governorGloss': u'supports', u'governor': 5, u'dependentGloss': u'.'}]}, {u'index': 1, u'enhancedDependencies': [{u'dep': u'ROOT', u'dependent': 3, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'introduces'}, {u'dep': u'nsubj', u'dependent': 1, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'BPS'}, {u'dep': u'nummod', u'dependent': 2, u'governorGloss': u'BPS', u'governor': 1, u'dependentGloss': u'3.5.0'}, {u'dep': u'compound', u'dependent': 4, u'governorGloss': u'support', u'governor': 5, u'dependentGloss': u'BPMN'}, {u'dep': u'dobj', u'dependent': 5, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'support'}, {u'dep': u'mark', u'dependent': 6, u'governorGloss': u'embedding', u'governor': 7, u'dependentGloss': u'by'}, {u'dep': u'advcl:by', u'dependent': 7, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'embedding'}, {u'dep': u'amod', u'dependent': 8, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'popular'}, {u'dep': u'compound', u'dependent': 9, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'Activiti'}, {u'dep': u'compound', u'dependent': 10, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'BPMN'}, {u'dep': u'dobj', u'dependent': 11, u'governorGloss': u'embedding', u'governor': 7, u'dependentGloss': u'engine'}, {u'dep': u'punct', u'dependent': 12, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'.'}], u'basicDependencies': [{u'dep': u'ROOT', u'dependent': 3, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'introduces'}, {u'dep': u'nsubj', u'dependent': 1, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'BPS'}, {u'dep': u'nummod', u'dependent': 2, u'governorGloss': u'BPS', u'governor': 1, u'dependentGloss': u'3.5.0'}, {u'dep': u'compound', u'dependent': 4, u'governorGloss': u'support', u'governor': 5, u'dependentGloss': u'BPMN'}, {u'dep': u'dobj', u'dependent': 5, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'support'}, {u'dep': u'mark', u'dependent': 6, u'governorGloss': u'embedding', u'governor': 7, u'dependentGloss': u'by'}, {u'dep': u'advcl', u'dependent': 7, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'embedding'}, {u'dep': u'amod', u'dependent': 8, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'popular'}, {u'dep': u'compound', u'dependent': 9, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'Activiti'}, {u'dep': u'compound', u'dependent': 10, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'BPMN'}, {u'dep': u'dobj', u'dependent': 11, u'governorGloss': u'embedding', u'governor': 7, u'dependentGloss': u'engine'}, {u'dep': u'punct', u'dependent': 12, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'.'}], u'tokens': [{u'index': 1, u'word': u'BPS', u'lemma': u'BPS', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 88, u'speaker': u'PER0', u'characterOffsetBegin': 85, u'originalText': u'BPS', u'ner': u'O', u'before': u' '}, {u'index': 2, u'word': u'3.5.0', u'lemma': u'3.5.0', u'after': u' ', u'pos': u'CD', u'characterOffsetEnd': 94, u'speaker': u'PER0', u'characterOffsetBegin': 89, u'originalText': u'3.5.0', u'ner': u'NUMBER', u'before': u' '}, {u'index': 3, u'word': u'introduces', u'lemma': u'introduce', u'after': u' \n    ', u'pos': u'VBZ', u'characterOffsetEnd': 105, u'speaker': u'PER0', u'characterOffsetBegin': 95, u'originalText': u'introduces', u'ner': u'O', u'before': u' '}, {u'index': 4, u'word': u'BPMN', u'lemma': u'BPMN', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 115, u'speaker': u'PER0', u'characterOffsetBegin': 111, u'originalText': u'BPMN', u'ner': u'O', u'before': u' \n    '}, {u'index': 5, u'word': u'support', u'lemma': u'support', u'after': u' ', u'pos': u'NN', u'characterOffsetEnd': 123, u'speaker': u'PER0', u'characterOffsetBegin': 116, u'originalText': u'support', u'ner': u'O', u'before': u' '}, {u'index': 6, u'word': u'by', u'lemma': u'by', u'after': u' ', u'pos': u'IN', u'characterOffsetEnd': 126, u'speaker': u'PER0', u'characterOffsetBegin': 124, u'originalText': u'by', u'ner': u'O', u'before': u' '}, {u'index': 7, u'word': u'embedding', u'lemma': u'embed', u'after': u' ', u'pos': u'VBG', u'characterOffsetEnd': 136, u'speaker': u'PER0', u'characterOffsetBegin': 127, u'originalText': u'embedding', u'ner': u'O', u'before': u' '}, {u'index': 8, u'word': u'popular', u'lemma': u'popular', u'after': u' ', u'pos': u'JJ', u'characterOffsetEnd': 144, u'speaker': u'PER0', u'characterOffsetBegin': 137, u'originalText': u'popular', u'ner': u'O', u'before': u' '}, {u'index': 9, u'word': u'Activiti', u'lemma': u'Activiti', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 153, u'speaker': u'PER0', u'characterOffsetBegin': 145, u'originalText': u'Activiti', u'ner': u'O', u'before': u' '}, {u'index': 10, u'word': u'BPMN', u'lemma': u'BPMN', u'after': u' ', u'pos': u'NNP', u'characterOffsetEnd': 158, u'speaker': u'PER0', u'characterOffsetBegin': 154, u'originalText': u'BPMN', u'ner': u'O', u'before': u' '}, {u'index': 11, u'word': u'engine', u'lemma': u'engine', u'after': u'', u'pos': u'NN', u'characterOffsetEnd': 165, u'speaker': u'PER0', u'characterOffsetBegin': 159, u'originalText': u'engine', u'ner': u'O', u'before': u' '}, {u'index': 12, u'word': u'.', u'lemma': u'.', u'after': u'', u'pos': u'.', u'characterOffsetEnd': 166, u'speaker': u'PER0', u'characterOffsetBegin': 165, u'originalText': u'.', u'ner': u'O', u'before': u''}], u'parse': u'(ROOT\n  (S\n    (NP (NNP BPS) (CD 3.5.0))\n    (VP (VBZ introduces)\n      (NP (NNP BPMN) (NN support))\n      (PP (IN by)\n        (S\n          (VP (VBG embedding)\n            (NP\n              (ADJP (JJ popular))\n              (NNP Activiti) (NNP BPMN) (NN engine))))))\n    (. .)))', u'enhancedPlusPlusDependencies': [{u'dep': u'ROOT', u'dependent': 3, u'governorGloss': u'ROOT', u'governor': 0, u'dependentGloss': u'introduces'}, {u'dep': u'nsubj', u'dependent': 1, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'BPS'}, {u'dep': u'nummod', u'dependent': 2, u'governorGloss': u'BPS', u'governor': 1, u'dependentGloss': u'3.5.0'}, {u'dep': u'compound', u'dependent': 4, u'governorGloss': u'support', u'governor': 5, u'dependentGloss': u'BPMN'}, {u'dep': u'dobj', u'dependent': 5, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'support'}, {u'dep': u'mark', u'dependent': 6, u'governorGloss': u'embedding', u'governor': 7, u'dependentGloss': u'by'}, {u'dep': u'advcl:by', u'dependent': 7, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'embedding'}, {u'dep': u'amod', u'dependent': 8, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'popular'}, {u'dep': u'compound', u'dependent': 9, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'Activiti'}, {u'dep': u'compound', u'dependent': 10, u'governorGloss': u'engine', u'governor': 11, u'dependentGloss': u'BPMN'}, {u'dep': u'dobj', u'dependent': 11, u'governorGloss': u'embedding', u'governor': 7, u'dependentGloss': u'engine'}, {u'dep': u'punct', u'dependent': 12, u'governorGloss': u'introduces', u'governor': 3, u'dependentGloss': u'.'}]}]}]
    print best_ans(q_deps, a_list_deps)


if __name__ == '__main__':
    test()