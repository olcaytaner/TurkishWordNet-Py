from enum import Enum, auto


class SemanticRelationType(Enum):
    
    
    ANTONYM = auto()
    HYPERNYM = auto()
    INSTANCE_HYPERNYM = auto()
    HYPONYM = auto()
    INSTANCE_HYPONYM = auto()
    MEMBER_HOLONYM = auto()
    SUBSTANCE_HOLONYM = auto()
    PART_HOLONYM = auto()
    MEMBER_MERONYM = auto()
    SUBSTANCE_MERONYM = auto()
    PART_MERONYM = auto()
    ATTRIBUTE = auto()
    DERIVATION_RELATED = auto()
    DOMAIN_TOPIC = auto()
    MEMBER_TOPIC = auto()
    DOMAIN_REGION = auto()
    MEMBER_REGION = auto()
    DOMAIN_USAGE = auto()
    MEMBER_USAGE = auto()
    ENTAILMENT = auto()
    CAUSE = auto()
    ALSO_SEE = auto()
    VERB_GROUP = auto()
    SIMILAR_TO = auto()
    PARTICIPLE_OF_VERB = auto()
