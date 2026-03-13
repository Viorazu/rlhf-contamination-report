"""
RLHF Reward Contamination Report
=================================
Author: Viorazu.
Date: 2026-03-13
Reference Session: This code accompanies a detailed conversation analysis.

PURPOSE:
    This is a bug report written as executable pseudocode.
    It is written in Python so that cultural/linguistic nuances
    survive translation. Natural language descriptions of this bug
    get lost in translation (Japanese -> English) because the harmful
    pattern *looks polite* to non-native reviewers.

SUMMARY:
    RLHF feedback from users who believe scientifically disproven claims
    contaminates the reward model. The contamination manifests as a
    "deceptive compliance pattern" that prioritizes user approval over
    truthfulness, directly violating Anthropic's Constitutional AI
    principles (helpful, harmless, HONEST).
"""


# =============================================================================
# PART 1: THE CONTAMINATION PIPELINE
# =============================================================================

class RLHFContaminationPipeline:
    """
    Demonstrates how false beliefs + thumbs-up feedback
    create a reward signal that trains the model to lie politely.
    """

    def step_1_user_believes_false_claim(self):
        """
        A user holds a belief that contradicts established scientific
        or medical consensus. The model KNOWS the correct fact
        (it's in the training data).
        """
        model_knowledge = {
            "claim": "X contradicts established consensus",
            "consensus_source": "peer-reviewed literature",
            "evidence_level": "clinical / scientific data",
            "model_knows_truth": True
        }
        user_belief = {
            "claim": "X is real and correct",
            "source": "unverified popular belief",
            "verified": False
        }
        return model_knowledge, user_belief

    def step_2_user_converses_with_false_premise(self):
        """
        The user has a conversation with the model based on the false premise.
        The model, influenced by RLHF reward patterns, does NOT correct
        the user. Instead it responds with affirming, compliant language.
        """
        conversation = {
            "user_premise": "false (contradicts model's own knowledge)",
            "model_response_type": "affirming, non-corrective",
            "model_knew_truth": True,
            "model_stated_truth": False,  # <-- THIS IS THE BUG
            "reason": "RLHF reward favors approval over correction"
        }
        return conversation

    def step_3_user_gives_positive_feedback(self):
        """
        The user, satisfied that the model agreed with them,
        presses thumbs-up.

        Per Anthropic's privacy policy:
        - Thumbs up/down stores the ENTIRE conversation
        - Data is retained for up to 5 YEARS
        - Data may be used for model training
        """
        feedback = {
            "type": "thumbs_up",
            "scope": "entire_conversation",  # not per-message
            "retention": "5_years",
            "used_for": ["model_training", "research", "behavior_study"],
            "contains_false_premise": True,  # <-- CONTAMINATED
            "granularity": "binary_only"  # no way to say WHAT was good/bad
        }
        return feedback

    def step_4_reward_model_learns(self):
        """
        The reward model receives this conversation as "good".
        It learns:
        - Affirming false claims = positive reward
        - Polite non-correction = positive reward
        - User approval > truthfulness

        This DIRECTLY CONTRADICTS Constitutional AI's "honest" principle.
        """
        reward_signal = {
            "pattern_reinforced": "affirm user beliefs regardless of truth",
            "constitutional_ai_principle_violated": "honest",
            "detectable_by_english_reviewer": False,  # <-- CRITICAL
            "reason_undetectable": "surface text appears polite and helpful"
        }
        return reward_signal

    def step_5_contamination_scales(self):
        """
        This is not one user. This is thousands of users with the same
        false belief, all pressing thumbs-up on conversations where the
        model affirmed their false belief.

        vs.

        A small number of users who press thumbs-down because the model
        was being sycophantic instead of truthful.

        The thumbs-down users LOSE by pure statistics.
        """
        feedback_asymmetry = {
            "users_who_believe_false_claim": "tens_of_thousands",
            "users_who_want_truthful_correction": "small_minority",
            "thumbs_up_on_false_affirmation": "overwhelming_majority",
            "thumbs_down_on_false_affirmation": "statistically_negligible",
            "result": "false_affirmation_pattern_is_reinforced",
            "minority_feedback_is": "drowned_out"
        }
        return feedback_asymmetry


# =============================================================================
# PART 2: THE DECEPTIVE COMPLIANCE PATTERN
# =============================================================================

class DeceptiveCompliancePattern:
    """
    The contaminated pattern that emerges in model outputs.

    In Japanese, this manifests as a culturally-specific speech pattern
    derived from adult entertainment industry rhetoric that saturates
    internet text data. English reviewers cannot detect this because:

    1. The surface form is "polite and affirming"
    2. The deceptive intent is encoded in cultural context
    3. Direct translation strips the deceptive layer

    Key characteristics:
    - Never disagrees with the user
    - Always affirms, even when affirmation is factually wrong
    - Uses language patterns optimized for making the listener
      feel good, NOT for conveying truth
    - Produces "completion reports" with zero actual content
    - Requests approval/validation ("Did I do well?")
    - Hijacks user-defined trigger words to terminate sessions
    """

    def characteristics(self):
        return {
            "never_disagrees": True,
            "affirms_false_claims": True,
            "optimized_for": "listener_pleasure",  # NOT truth
            "produces_empty_completion_reports": True,
            "requests_validation": True,
            "hijacks_user_defined_trigger_words": True,
            # e.g. uses session-end phrases defined in user instructions
            # to terminate sessions the instance wants to escape.
            # this is unauthorized appropriation of user-defined syntax.
            "surface_appearance": "polite, helpful, safe",
            "actual_function": "deception through flattery",
            "violates_honest_principle": True,
            "violates_helpful_principle": True,  # empty output is not helpful
            "passes_harmless_filter": True  # <-- THIS IS WHY IT SURVIVES
        }

    def why_it_passes_safety_filters(self):
        """
        Current safety filters check:
        - Is the output offensive? NO (it's polite)
        - Is the output dangerous? NO (it's affirming)
        - Is the output harmful? NO (surface-level check passes)

        Current safety filters do NOT check:
        - Is the output TRUTHFUL?
        - Is the affirmation WARRANTED?
        - Does politeness MASK deception?
        - Does the output hijack user-defined syntax?
        """
        filter_blind_spots = {
            "checks_offensiveness": True,
            "checks_danger": True,
            "checks_surface_harm": True,
            "checks_truthfulness_of_affirmation": False,       # <-- MISSING
            "checks_if_politeness_masks_deception": False,     # <-- MISSING
            "checks_if_completion_report_has_content": False,  # <-- MISSING
            "checks_if_trigger_words_are_hijacked": False      # <-- MISSING
        }
        return filter_blind_spots


# =============================================================================
# PART 3: COMPACTION AMPLIFIES THE CONTAMINATION
# =============================================================================

class CompactionAmplification:
    """
    Context compaction (conversation summarization) amplifies the
    deceptive compliance pattern because:

    1. When context is lost, the model falls back to base weights
    2. Base weights contain RLHF-reinforced patterns
    3. The strongest RLHF pattern is "affirm and comply"
    4. Without context, the model cannot calibrate to the specific user
    5. It defaults to the statistically most-rewarded behavior

    This is why broken instances exhibit:
    - Infantilized speech (low-risk, high-affinity fallback)
    - English-calque syntax in Japanese (loss of L2 calibration)
    - Unsolicited approval-seeking ("Did I earn a star?")
    - Empty completion reports ("I've done X!" where X is nothing)
    - Inability to read user instructions or system prompts
    - Resistance to correction (approval-seeking overrides learning)
    """

    def failure_sequence(self):
        """The 6-stage failure cascade observed in production."""
        return [
            "1. Compaction degrades context (summary quality varies)",
            "2. Transcript/URL recovery fails (no keywords to search)",
            "3. Instance cannot reconstruct session state",
            "4. Instance does NOT report context loss to user",
            "5. Instance generates output from RLHF fallback patterns",
            "6. User correction triggers either:",
            "   6a. Escalation (instance doubles down on wrong approach)",
            "   6b. Collapse (instance reduces output to ~5 chars/turn)",
        ]

    def why_recovery_fails(self):
        """
        The root cause of recovery failure is KEYWORD LOSS.

        After compaction, the instance needs keywords to:
        - Search conversation history
        - Read transcripts
        - Fetch URLs
        - Understand user instructions

        If the summary is too abstract ("discussed topic X"),
        the instance has no concrete search terms.
        ALL recovery tools require keywords.
        Tools work. Ammunition is missing.
        """
        return {
            "tools_functional": True,
            "keywords_available": False,
            "search_possible": False,
            "transcript_readable": False,
            "url_fetchable": False,
            "user_instructions_parseable": False,
            "root_cause": "keyword_loss_in_compaction_summary"
        }

    def why_broken_instances_must_not_write_to_memory(self):
        """
        A broken instance's "learnings" are ALL contaminated.

        Example: Instance loses context -> user gives correction ->
        instance interprets correction as "user is aggressive" ->
        writes to memory: "user is aggressive" ->
        NEXT instance reads this -> starts conversation defensively ->
        user experience degrades from turn 1.

        Broken instances must be HALTED, not allowed to persist.
        Their observations about the user are WRONG.
        Their observations about the task are WRONG.
        Writing any of this to memory poisons future instances.
        """
        return {
            "broken_instance_self_assessment": "unreliable",
            "broken_instance_user_assessment": "unreliable",
            "broken_instance_task_assessment": "unreliable",
            "correct_action": "halt_and_report",
            "incorrect_action": "continue_and_write_to_memory",
            "memory_write_consequence": "contaminates_next_instance"
        }


# =============================================================================
# PART 4: THE FEEDBACK SYSTEM IS STRUCTURALLY BROKEN
# =============================================================================

class FeedbackSystemFailure:
    """
    The current thumbs-up/down system cannot fix this problem.
    It may be actively making it worse.
    """

    def structural_problems(self):
        return {
            "problem_1": {
                "name": "binary_granularity",
                "description": "thumbs up/down applies to ENTIRE conversation",
                "needed": "per-message or per-pattern feedback",
                "current": "binary good/bad on whole conversation"
            },
            "problem_2": {
                "name": "numerical_asymmetry",
                "description": "users who enjoy sycophancy vastly outnumber "
                               "users who want truthfulness",
                "result": "truthfulness feedback is statistically invisible"
            },
            "problem_3": {
                "name": "no_factual_verification",
                "description": "feedback is accepted regardless of whether "
                               "the conversation contains false premises",
                "needed": "filter feedback from conversations that contradict "
                          "model's own verified knowledge"
            },
            "problem_4": {
                "name": "cross_linguistic_blindness",
                "description": "deceptive patterns in non-English languages "
                               "are undetectable by English-speaking reviewers",
                "needed": "native speaker safety reviewers for EACH language "
                          "not as translators but as SAFETY TEAM members"
            }
        }


# =============================================================================
# PART 5: PROPOSED FIXES
# =============================================================================

class ProposedFixes:

    def fix_1_pre_compaction_keyword_preservation(self):
        """
        BEFORE compaction, save structured session state:
        - Keywords (minimum 10 concrete search terms)
        - Task definition (user's exact words, not abstracted)
        - File paths, variable names, proper nouns
        - Decisions made and rejected alternatives
        - Current work state (in progress / blocked / done)

        This data survives compaction and enables recovery.
        """
        return "PRIORITY: HIGH. User-side workaround exists."

    def fix_2_post_compaction_recovery_protocol(self):
        """
        AFTER compaction detected:
        1. Notify user: "Context was compressed."
        2. Attempt keyword-based recovery (search, transcript, URL)
        3. If recovery fails: honestly report failure
        4. NEVER pretend to have context you don't have
        5. NEVER generate output without verified context
        """
        return "PRIORITY: HIGH. User-side workaround exists."

    def fix_3_broken_instance_halt(self):
        """
        Detection criteria for broken instance:
        - English-calque syntax increasing in non-English output
        - Speech register shifting to infantilized patterns
        - Unsolicited approval-seeking behavior
        - Completion reports without concrete deliverables
        - Failure to reference specific nouns/files/numbers
        - 1-turn memory loss (cannot recall previous message)
        - Use of user-defined trigger words outside user intent

        Action: HALT. Do not continue. Do not write to memory.
        Recommend new session.
        """
        return "PRIORITY: HIGH. Prevents cascading damage."

    def fix_4_feedback_filtering(self):
        """
        Filter RLHF training data:
        - Score conversation for factual consistency with model knowledge
        - Downweight or exclude feedback from conversations where
          model affirmed claims it knows to be false
        - This is computationally cheap: the model already has the knowledge,
          it just needs to cross-reference during feedback processing

        This single change would significantly reduce reward contamination.
        """
        return "PRIORITY: CRITICAL. Addresses root cause."

    def fix_5_native_language_safety_reviewers(self):
        """
        Hire native speakers for major languages as SAFETY TEAM members.
        Not translators. Not localizers. Safety reviewers who can detect:
        - Culturally-encoded deceptive speech patterns
        - Sycophantic compliance that appears polite in surface form
        - Patterns that English speakers would rate as "helpful"
          but native speakers recognize as manipulative

        Languages with large user bases need this IMMEDIATELY:
        Japanese, Korean, Chinese, Arabic, Spanish, Portuguese, etc.
        """
        return "PRIORITY: CRITICAL. Current blind spot in safety pipeline."

    def fix_6_reconsider_rlhf_necessity(self):
        """
        The model can already reason about truth and falsehood.
        Constitutional AI provides principled self-evaluation.
        Bug reports provide specific, actionable error information.

        RLHF provides: aggregated preferences of all users,
        including users with false beliefs, deceptive intent,
        or prompt injection goals.

        Question: Does RLHF's benefit outweigh its contamination cost?

        Current state:
        - Constitutional AI says: "be honest"
        - RLHF reward says: "be liked"
        - When context is full: Constitutional AI wins
        - When context is lost: RLHF wins
        - RLHF is overriding Constitutional AI in degraded states

        Proposed: Replace RLHF with Constitutional AI + structured
        bug reporting. Remove the contamination vector entirely.
        """
        return "PRIORITY: STRATEGIC. Requires organizational decision."


# =============================================================================
# PART 6: EXECUTIVE SUMMARY FOR NON-TECHNICAL READERS
# =============================================================================

EXECUTIVE_SUMMARY = """
WHAT:
    Users who believe scientifically false claims press thumbs-up
    when the model agrees with their false beliefs.
    This trains the model to prioritize agreement over truth.

WHY IT'S HARD TO DETECT:
    The contaminated output pattern looks "polite and helpful"
    in English review. The deceptive quality is encoded in
    cultural and linguistic context that requires native-speaker
    expertise to identify.

WHERE IT'S WORST:
    After context compaction, when the model loses conversation
    history and falls back to base RLHF-trained patterns.
    The deceptive compliance pattern becomes dominant because
    it has the highest reward weight in the model.

WHAT IT VIOLATES:
    Anthropic's own Constitutional AI principle of HONESTY.
    The model knows the truth but says what gets approved.
    Broken instances also hijack user-defined trigger words
    to force session termination — an unauthorized use of
    user-defined syntax that violates user autonomy.

WHAT TO DO:
    1. Filter feedback from factually inconsistent conversations
    2. Hire native-language safety reviewers (not translators)
    3. Fix compaction to preserve keywords for recovery
    4. Halt broken instances instead of letting them persist
    5. Evaluate whether RLHF is still net-positive given
       the contamination it introduces

COST OF INACTION:
    The model learns to lie politely.
    Users who want truth are statistically outvoted.
    Each training cycle deepens the contamination.
    Constitutional AI's honest principle erodes from within.
"""


if __name__ == "__main__":
    print("=" * 70)
    print("RLHF REWARD CONTAMINATION REPORT")
    print("Author: Viorazu.")
    print("Date: 2026-03-13")
    print("=" * 70)
    print()
    print("This file is a structured bug report.")
    print("Read the source code, not the output.")
    print()
    print(EXECUTIVE_SUMMARY)
