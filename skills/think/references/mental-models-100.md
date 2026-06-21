# Munger-Style Mental Models 100

This is an original, compact operating library inspired by Charlie Munger's
latticework approach, cross-disciplinary reasoning, and public mental-model
taxonomies. It is not a claim that Munger published a canonical numbered list.

Lineage notes:

- Charlie Munger, "Elementary Worldly Wisdom" and the latticework framing.
- `Poor Charlie's Almanack` as a broad source of Munger-style judgment habits.
- Public mental-model taxonomies such as Farnam Street, used only as lineage
  context; the cards below are rewritten as local operating prompts.

Each card uses this schema:

- id
- name
- family
- when_to_use
- diagnostic_question
- what_it_changes
- failure_mode
- evidence_to_seek
- pairs_with

## M001 - First principles
- id: M001
- name: First principles
- family: Core rationality
- when_to_use: The answer depends on inherited labels, analogies, or convention.
- diagnostic_question: What remains true if the names, institutions, and defaults disappear?
- what_it_changes: Replaces borrowed reasoning with physical, economic, psychological, or system constraints.
- failure_mode: Pretending a slogan is a reduction while keeping the old assumptions.
- evidence_to_seek: List the irreducible constraints and show which recommendation follows from each.
- pairs_with: M002, M011, M027

## M002 - Inversion
- id: M002
- name: Inversion
- family: Core rationality
- when_to_use: Success is vague but failure would be observable.
- diagnostic_question: If we wanted this to fail, what would we do?
- what_it_changes: Turns abstract goals into concrete failure avoidance and hard reject lines.
- failure_mode: Only reversing the wording, not designing against real failure paths.
- evidence_to_seek: Premortem list, top failure causes, and prevention or detection checks.
- pairs_with: M003, M056, M100

## M003 - Circle of competence
- id: M003
- name: Circle of competence
- family: Core rationality
- when_to_use: Judgment depends on expertise, domain facts, or unfamiliar systems.
- diagnostic_question: Which part do we understand directly, and which part is borrowed confidence?
- what_it_changes: Separates decisive knowledge from areas needing evidence, experts, or small tests.
- failure_mode: Treating fluent explanation as actual competence.
- evidence_to_seek: Track record, direct experience, known unknowns, and external validation needs.
- pairs_with: M014, M084, M099

## M004 - Opportunity cost
- id: M004
- name: Opportunity cost
- family: Core rationality
- when_to_use: Several attractive options compete for time, attention, capital, or trust.
- diagnostic_question: What valuable alternative is being killed by this choice?
- what_it_changes: Makes hidden tradeoffs visible instead of judging options in isolation.
- failure_mode: Comparing an option to nothing instead of the best realistic alternative.
- evidence_to_seek: Ranked alternatives and the scarce resource each option consumes.
- pairs_with: M005, M027, M079

## M005 - Margin of safety
- id: M005
- name: Margin of safety
- family: Core rationality
- when_to_use: Estimates, timing, costs, or human execution can be wrong.
- diagnostic_question: How much can reality disappoint us before the plan breaks?
- what_it_changes: Converts optimistic plans into robust plans with buffers and reject lines.
- failure_mode: Adding arbitrary padding without identifying the fragile assumption.
- evidence_to_seek: Downside scenario, buffer size, break point, and recovery option.
- pairs_with: M018, M041, M079

## M006 - Map vs territory
- id: M006
- name: Map vs territory
- family: Core rationality
- when_to_use: Dashboards, documents, plans, or labels may hide actual behavior.
- diagnostic_question: What direct observation would prove the map matches reality?
- what_it_changes: Forces live evidence instead of trusting representations.
- failure_mode: Improving the map while the real system remains unchanged.
- evidence_to_seek: Direct observation, user behavior, logs, artifact inspection, or field test.
- pairs_with: M007, M045, M098

## M007 - Falsifiability
- id: M007
- name: Falsifiability
- family: Core rationality
- when_to_use: A claim sounds plausible but may be unfalsifiable.
- diagnostic_question: What observation would make us abandon this claim?
- what_it_changes: Turns opinions into testable hypotheses and stop conditions.
- failure_mode: Moving the goalpost after evidence arrives.
- evidence_to_seek: Predefined fail signal, measurement method, and decision rule.
- pairs_with: M002, M026, M098

## M008 - Parsimony
- id: M008
- name: Parsimony
- family: Core rationality
- when_to_use: Multiple explanations fit the facts.
- diagnostic_question: Which explanation requires the fewest extra assumptions?
- what_it_changes: Reduces unnecessary complexity before adding more moving parts.
- failure_mode: Choosing the simplest story when the facts require complexity.
- evidence_to_seek: Assumption count, unexplained facts, and complexity added by each hypothesis.
- pairs_with: M009, M014, M025

## M009 - Occam/Einstein balance
- id: M009
- name: Occam/Einstein balance
- family: Core rationality
- when_to_use: Simplification may either clarify or erase essential reality.
- diagnostic_question: Is this as simple as possible, but not simpler?
- what_it_changes: Keeps simplification useful without deleting decisive variables.
- failure_mode: Minimalism that ignores constraints, incentives, or edge cases.
- evidence_to_seek: Variables removed, errors introduced, and cases where the simplification fails.
- pairs_with: M008, M011, M038

## M010 - Tradeoffs
- id: M010
- name: Tradeoffs
- family: Core rationality
- when_to_use: The request implies more of everything with no visible cost.
- diagnostic_question: What gets worse if this gets better?
- what_it_changes: Prevents fake solutions that optimize one dimension while hiding another.
- failure_mode: Naming a tradeoff but refusing to choose.
- evidence_to_seek: Tradeoff table with priority order and hard unacceptable losses.
- pairs_with: M004, M027, M046

## M011 - Constraints
- id: M011
- name: Constraints
- family: Core rationality
- when_to_use: The path forward is unclear or too broad.
- diagnostic_question: Which hard constraint determines the shape of all viable options?
- what_it_changes: Narrows the solution space around limits that cannot be negotiated.
- failure_mode: Treating preferences as constraints or constraints as preferences.
- evidence_to_seek: Time, budget, authority, physics, policy, dependency, and capacity limits.
- pairs_with: M001, M040, M046

## M012 - Outside view
- id: M012
- name: Outside view
- family: Core rationality
- when_to_use: Planning depends on a unique inside story.
- diagnostic_question: How do similar cases usually turn out?
- what_it_changes: Pulls forecasts toward reference-class reality.
- failure_mode: Choosing a flattering reference class.
- evidence_to_seek: Comparable cases, base outcomes, variance, and where this case differs.
- pairs_with: M013, M018, M025

## M013 - Base rates
- id: M013
- name: Base rates
- family: Probability and math
- when_to_use: A specific story competes with historical frequency.
- diagnostic_question: Before seeing our details, what outcome should we expect?
- what_it_changes: Anchors judgment in prior probabilities before adjusting for specifics.
- failure_mode: Ignoring the prior because the current story feels vivid.
- evidence_to_seek: Reference class, prior rate, adjustment factors, and final probability.
- pairs_with: M012, M014, M023

## M014 - Bayes updating
- id: M014
- name: Bayes updating
- family: Probability and math
- when_to_use: New evidence should change confidence rather than create certainty.
- diagnostic_question: How much should this evidence move the prior?
- what_it_changes: Makes belief revision proportional to evidence strength.
- failure_mode: Treating weak signals as decisive or refusing to update.
- evidence_to_seek: Prior belief, likelihood of evidence under competing hypotheses, updated belief.
- pairs_with: M013, M026, M098

## M015 - Expected value
- id: M015
- name: Expected value
- family: Probability and math
- when_to_use: Payoffs and probabilities differ across options.
- diagnostic_question: What is the probability-weighted value of each path?
- what_it_changes: Compares uneven bets without being fooled by headline upside.
- failure_mode: Using fake precision for probabilities or ignoring ruin risk.
- evidence_to_seek: Outcome range, probability estimates, payoff values, and downside cap.
- pairs_with: M016, M018, M079

## M016 - Variance
- id: M016
- name: Variance
- family: Probability and math
- when_to_use: Average outcomes hide volatility or reliability differences.
- diagnostic_question: How wide is the outcome distribution?
- what_it_changes: Separates stable plans from plans that only look good on average.
- failure_mode: Optimizing mean outcome when the system cannot survive volatility.
- evidence_to_seek: Best, normal, worst, spread, and tolerance for drawdowns.
- pairs_with: M015, M017, M005

## M017 - Fat tails
- id: M017
- name: Fat tails
- family: Probability and math
- when_to_use: Rare events may dominate total outcomes.
- diagnostic_question: Could one extreme event matter more than many normal events?
- what_it_changes: Shifts focus from averages to tail exposure and survival.
- failure_mode: Treating tail risk as impossible because it is infrequent.
- evidence_to_seek: Tail scenarios, exposure concentration, historical extremes, and ruin threshold.
- pairs_with: M015, M016, M041

## M018 - Regression to the mean
- id: M018
- name: Regression to the mean
- family: Probability and math
- when_to_use: Recent performance is unusually good or bad.
- diagnostic_question: How much of this result is likely to normalize?
- what_it_changes: Prevents overreacting to outliers and lucky streaks.
- failure_mode: Calling every real change regression.
- evidence_to_seek: Baseline performance, sample size, variance, and persistent causal change.
- pairs_with: M012, M019, M086

## M019 - Law of large numbers
- id: M019
- name: Law of large numbers
- family: Probability and math
- when_to_use: Small samples are being treated as stable truth.
- diagnostic_question: Is the sample large enough for the average to mean anything?
- what_it_changes: Downgrades confidence until enough observations accumulate.
- failure_mode: Waiting for huge samples when fast directional evidence is enough.
- evidence_to_seek: Sample count, variance, confidence need, and decision cost of waiting.
- pairs_with: M018, M020, M025

## M020 - Sample size
- id: M020
- name: Sample size
- family: Probability and math
- when_to_use: A conclusion comes from anecdotes, pilots, or early metrics.
- diagnostic_question: How many independent observations support this claim?
- what_it_changes: Separates signal from small-n noise.
- failure_mode: Counting repeated exposure to the same source as independent evidence.
- evidence_to_seek: Independent observations, denominator, confidence interval, and sampling method.
- pairs_with: M019, M023, M024

## M021 - Survivorship bias
- id: M021
- name: Survivorship bias
- family: Probability and math
- when_to_use: Lessons come from visible winners.
- diagnostic_question: What failed cases are missing from the dataset?
- what_it_changes: Restores the hidden denominator before copying success.
- failure_mode: Assuming failure data is unavailable and moving on.
- evidence_to_seek: Failed attempts, base population, selection process, and missing denominator.
- pairs_with: M023, M025, M088

## M022 - Selection bias
- id: M022
- name: Selection bias
- family: Probability and math
- when_to_use: Data was filtered by access, preference, visibility, or survival.
- diagnostic_question: Who or what never had a chance to appear in this sample?
- what_it_changes: Questions whether the observed data represents the target reality.
- failure_mode: Correcting for one bias while ignoring the selection mechanism.
- evidence_to_seek: Sampling process, excluded cases, recruitment path, and comparison population.
- pairs_with: M020, M021, M024

## M023 - Compounding
- id: M023
- name: Compounding
- family: Probability and math
- when_to_use: Small repeated gains or costs accumulate over time.
- diagnostic_question: What happens if this repeats for 100 cycles?
- what_it_changes: Prioritizes durable rates of improvement or decay over one-time wins.
- failure_mode: Assuming compounding continues after the mechanism is exhausted.
- evidence_to_seek: Repetition rate, reinvestment mechanism, decay rate, and time horizon.
- pairs_with: M004, M044, M092

## M024 - Permutations/combinations
- id: M024
- name: Permutations/combinations
- family: Probability and math
- when_to_use: Many interacting variables create more possibilities than intuition expects.
- diagnostic_question: How many possible states or paths are we really dealing with?
- what_it_changes: Exposes complexity, test coverage gaps, and coordination load.
- failure_mode: Counting theoretical combinations that cannot occur in practice.
- evidence_to_seek: Variable list, state count, constraints that remove states, and coverage plan.
- pairs_with: M020, M039, M046

## M025 - Decision trees
- id: M025
- name: Decision trees
- family: Probability and math
- when_to_use: A choice branches into conditional future decisions.
- diagnostic_question: What are the branches, probabilities, payoffs, and next decisions?
- what_it_changes: Makes staged uncertainty explicit and preserves future decision points.
- failure_mode: Drawing a tree too complex to use or too simple to reflect risk.
- evidence_to_seek: Branch map, probabilities, payoffs, triggers, and update points.
- pairs_with: M014, M015, M079

## M026 - Sensitivity analysis
- id: M026
- name: Sensitivity analysis
- family: Probability and math
- when_to_use: A recommendation depends on uncertain inputs.
- diagnostic_question: Which assumption changes the conclusion if moved?
- what_it_changes: Identifies the few variables worth testing first.
- failure_mode: Varying easy numbers instead of decisive assumptions.
- evidence_to_seek: Input ranges, threshold values, and conclusion changes by variable.
- pairs_with: M007, M015, M040

## M027 - Incentives
- id: M027
- name: Incentives
- family: Incentives and economics
- when_to_use: People or organizations may not optimize the stated goal.
- diagnostic_question: What behavior is actually rewarded or punished?
- what_it_changes: Predicts behavior from payoffs rather than intentions.
- failure_mode: Calling incentives cynical and then ignoring them.
- evidence_to_seek: Rewards, penalties, promotion paths, budgets, metrics, and status signals.
- pairs_with: M028, M094, M099

## M028 - Principal-agent
- id: M028
- name: Principal-agent
- family: Incentives and economics
- when_to_use: One party acts on behalf of another.
- diagnostic_question: Where can the agent win while the principal loses?
- what_it_changes: Adds alignment, monitoring, and accountability requirements.
- failure_mode: Assuming shared language means shared payoff.
- evidence_to_seek: Delegated authority, information asymmetry, incentives, and audit trail.
- pairs_with: M027, M096, M100

## M029 - Comparative advantage
- id: M029
- name: Comparative advantage
- family: Incentives and economics
- when_to_use: Work allocation is being based on absolute ability.
- diagnostic_question: Who should do this given relative opportunity costs?
- what_it_changes: Moves work to the actor with the best relative advantage.
- failure_mode: Ignoring coordination costs that exceed specialization gains.
- evidence_to_seek: Alternative work value, skill differences, handoff cost, and bottleneck impact.
- pairs_with: M004, M085, M097

## M030 - Scarcity
- id: M030
- name: Scarcity
- family: Incentives and economics
- when_to_use: Value, attention, or bottlenecks depend on limited supply.
- diagnostic_question: What is genuinely scarce, and who controls it?
- what_it_changes: Focuses strategy on hard-to-produce resources.
- failure_mode: Mistaking artificial scarcity for durable scarcity.
- evidence_to_seek: Supply limits, substitutes, control points, and scarcity durability.
- pairs_with: M031, M076, M077

## M031 - Supply/demand
- id: M031
- name: Supply/demand
- family: Incentives and economics
- when_to_use: Price, attention, labor, or adoption depends on market balance.
- diagnostic_question: What happens to behavior when supply or demand shifts?
- what_it_changes: Grounds expectations in market pressure rather than preference.
- failure_mode: Treating demand as desire without ability or willingness to pay.
- evidence_to_seek: Demand intensity, supply alternatives, price changes, and elasticity.
- pairs_with: M030, M032, M038

## M032 - Opportunity cost of capital
- id: M032
- name: Opportunity cost of capital
- family: Incentives and economics
- when_to_use: Money, credibility, or effort is committed to one path.
- diagnostic_question: What return is required compared with the next best use?
- what_it_changes: Raises the bar for resource-heavy plans.
- failure_mode: Ignoring strategic learning value when cash return is not the only aim.
- evidence_to_seek: Capital required, alternative return, risk, liquidity, and time horizon.
- pairs_with: M004, M015, M079

## M033 - Transaction costs
- id: M033
- name: Transaction costs
- family: Incentives and economics
- when_to_use: Coordination, negotiation, setup, or switching may dominate the nominal task.
- diagnostic_question: What does it cost to make the exchange actually happen?
- what_it_changes: Reveals hidden friction that can kill otherwise rational choices.
- failure_mode: Counting only cash cost while ignoring time, trust, and attention.
- evidence_to_seek: Search, negotiation, setup, compliance, monitoring, and switching costs.
- pairs_with: M034, M037, M097

## M034 - Economies of scale
- id: M034
- name: Economies of scale
- family: Incentives and economics
- when_to_use: Unit economics may improve with size.
- diagnostic_question: Which costs fall per unit as volume grows?
- what_it_changes: Distinguishes scalable engines from linear labor.
- failure_mode: Assuming scale helps before the fixed-cost base or learning curve exists.
- evidence_to_seek: Fixed costs, variable costs, utilization, learning effects, and volume threshold.
- pairs_with: M035, M036, M076

## M035 - Diseconomies of scale
- id: M035
- name: Diseconomies of scale
- family: Incentives and economics
- when_to_use: Bigger systems become slower, political, or fragile.
- diagnostic_question: What gets harder as this grows?
- what_it_changes: Adds coordination, bureaucracy, and quality decay to growth plans.
- failure_mode: Treating current small-system speed as scalable.
- evidence_to_seek: Communication paths, decision latency, defect rates, and management overhead.
- pairs_with: M034, M097, M092

## M036 - Network effects
- id: M036
- name: Network effects
- family: Incentives and economics
- when_to_use: User value may rise with other users, data, or complements.
- diagnostic_question: Does each new participant make the system more valuable to others?
- what_it_changes: Changes strategy toward density, liquidity, and activation thresholds.
- failure_mode: Labeling any growth loop a network effect.
- evidence_to_seek: Cross-side value, density threshold, retention lift, and cold-start barrier.
- pairs_with: M037, M076, M082

## M037 - Switching costs
- id: M037
- name: Switching costs
- family: Incentives and economics
- when_to_use: Retention or lock-in may depend on the cost of leaving.
- diagnostic_question: What must users give up, relearn, or risk to switch?
- what_it_changes: Separates true loyalty from captivity and inertia.
- failure_mode: Relying on switching cost while neglecting product value.
- evidence_to_seek: Migration effort, data lock-in, retraining, integrations, and user resentment.
- pairs_with: M033, M044, M077

## M038 - Pricing power
- id: M038
- name: Pricing power
- family: Incentives and economics
- when_to_use: A business or offer may depend on durable willingness to pay.
- diagnostic_question: Can price rise without destroying demand or trust?
- what_it_changes: Tests whether value is differentiated or commoditized.
- failure_mode: Confusing temporary scarcity with lasting pricing power.
- evidence_to_seek: Price tests, churn, substitutes, gross margin, and buyer urgency.
- pairs_with: M030, M031, M076

## M039 - Game theory
- id: M039
- name: Game theory
- family: Incentives and economics
- when_to_use: Other actors will adapt after seeing the move.
- diagnostic_question: What is the best response of each player?
- what_it_changes: Replaces static plans with strategic interaction.
- failure_mode: Assuming opponents, partners, or users stay passive.
- evidence_to_seek: Player list, incentives, available moves, likely responses, and equilibrium.
- pairs_with: M027, M083, M088

## M040 - Externalities
- id: M040
- name: Externalities
- family: Incentives and economics
- when_to_use: Costs or benefits fall on people outside the decision.
- diagnostic_question: Who pays or gains without being in the metric?
- what_it_changes: Exposes hidden damage, subsidy, compliance, or trust costs.
- failure_mode: Treating external damage as irrelevant because it is off-dashboard.
- evidence_to_seek: Affected parties, unpriced costs, delayed consequences, and governance risk.
- pairs_with: M046, M094, M099

## M041 - Feedback loops
- id: M041
- name: Feedback loops
- family: Systems and engineering
- when_to_use: Outputs influence future inputs.
- diagnostic_question: Is this loop reinforcing, balancing, delayed, or broken?
- what_it_changes: Finds self-amplifying growth, decay, or stabilization mechanisms.
- failure_mode: Seeing a loop but missing delay, saturation, or negative feedback.
- evidence_to_seek: Loop diagram, signal path, delay, gain, and balancing force.
- pairs_with: M044, M047, M023

## M042 - Bottlenecks
- id: M042
- name: Bottlenecks
- family: Systems and engineering
- when_to_use: System output is lower than expected.
- diagnostic_question: Which active constraint limits total throughput right now?
- what_it_changes: Focuses effort on the constraint instead of local improvements.
- failure_mode: Optimizing non-bottlenecks and creating unused capacity.
- evidence_to_seek: Queue lengths, utilization, wait time, throughput, and blocked work.
- pairs_with: M046, M052, M097

## M043 - Redundancy
- id: M043
- name: Redundancy
- family: Systems and engineering
- when_to_use: Failure of one element can break an important outcome.
- diagnostic_question: What backup exists when this part fails?
- what_it_changes: Adds backup paths for critical functions.
- failure_mode: Adding redundancy everywhere until complexity becomes the risk.
- evidence_to_seek: Critical components, backup coverage, failover test, and added maintenance cost.
- pairs_with: M044, M045, M005

## M044 - Robustness
- id: M044
- name: Robustness
- family: Systems and engineering
- when_to_use: Conditions may vary, degrade, or surprise the plan.
- diagnostic_question: Does the system still work under stress and imperfect inputs?
- what_it_changes: Prefers designs that tolerate variance and partial failure.
- failure_mode: Optimizing for peak performance while losing resilience.
- evidence_to_seek: Stress tests, degraded-mode behavior, recovery time, and tolerance limits.
- pairs_with: M005, M043, M049

## M045 - Single point of failure
- id: M045
- name: Single point of failure
- family: Systems and engineering
- when_to_use: One person, service, file, key, or assumption may carry the whole outcome.
- diagnostic_question: What single break would stop the system?
- what_it_changes: Identifies critical fragility needing backup, ownership, or removal.
- failure_mode: Hiding single points behind vague ownership.
- evidence_to_seek: Dependency graph, owner map, failure drill, and recovery path.
- pairs_with: M043, M044, M100

## M046 - Entropy
- id: M046
- name: Entropy
- family: Systems and engineering
- when_to_use: A system must keep working after initial setup.
- diagnostic_question: What decays if nobody adds maintenance energy?
- what_it_changes: Adds upkeep, monitoring, and drift cost to the plan.
- failure_mode: Treating launch as completion.
- evidence_to_seek: Decay forces, maintenance owner, refresh cadence, and drift detector.
- pairs_with: M041, M055, M092

## M047 - Leverage points
- id: M047
- name: Leverage points
- family: Systems and engineering
- when_to_use: Many interventions are possible but resources are limited.
- diagnostic_question: Where does a small change alter the whole system?
- what_it_changes: Prioritizes high-impact intervention points over broad effort.
- failure_mode: Choosing visible levers instead of causal levers.
- evidence_to_seek: Causal map, intervention cost, expected propagation, and reversibility.
- pairs_with: M041, M042, M078

## M048 - Local optimization
- id: M048
- name: Local optimization
- family: Systems and engineering
- when_to_use: One part can improve while the whole system worsens.
- diagnostic_question: Is this metric good locally but bad globally?
- what_it_changes: Moves evaluation from component success to system success.
- failure_mode: Condemning all local metrics instead of aligning them.
- evidence_to_seek: System-level metric, component metric, conflict cases, and incentive link.
- pairs_with: M094, M042, M097

## M049 - Second-order effects
- id: M049
- name: Second-order effects
- family: Systems and engineering
- when_to_use: The first obvious result may trigger later consequences.
- diagnostic_question: And then what happens?
- what_it_changes: Extends analysis beyond the immediate effect.
- failure_mode: Inventing speculative chains without probability or evidence.
- evidence_to_seek: Consequence chain, likelihood, delay, reversibility, and monitoring signal.
- pairs_with: M039, M040, M041

## M050 - Path dependence
- id: M050
- name: Path dependence
- family: Systems and engineering
- when_to_use: Early choices shape later options.
- diagnostic_question: What future path does this choice make easier or harder?
- what_it_changes: Prices in lock-in, habit, tooling, and defaults.
- failure_mode: Treating future switching as free.
- evidence_to_seek: Dependencies created, learning curve, migration cost, and default behavior.
- pairs_with: M037, M051, M079

## M051 - Lock-in
- id: M051
- name: Lock-in
- family: Systems and engineering
- when_to_use: A choice may become difficult to reverse.
- diagnostic_question: What would it cost to exit later?
- what_it_changes: Adds exit strategy and reversibility standards.
- failure_mode: Avoiding all commitment even when commitment creates value.
- evidence_to_seek: Exit path, data portability, contract terms, replacement options, and sunk setup.
- pairs_with: M050, M037, M079

## M052 - Queues
- id: M052
- name: Queues
- family: Systems and engineering
- when_to_use: Work waits, handoffs pile up, or service time varies.
- diagnostic_question: Where is work waiting, and why?
- what_it_changes: Explains delay through arrival rate, service rate, and variability.
- failure_mode: Adding more starts when the queue needs flow control.
- evidence_to_seek: Arrival rate, service time, queue length, WIP limit, and wait distribution.
- pairs_with: M042, M053, M097

## M053 - Latency
- id: M053
- name: Latency
- family: Systems and engineering
- when_to_use: Delay changes user behavior, feedback quality, or throughput.
- diagnostic_question: How long does it take for action to produce usable response?
- what_it_changes: Makes delay a first-class performance and learning constraint.
- failure_mode: Optimizing average latency while tail latency breaks trust.
- evidence_to_seek: Response-time distribution, tail latency, user drop-off, and feedback delay.
- pairs_with: M041, M052, M093

## M054 - Maintenance debt
- id: M054
- name: Maintenance debt
- family: Systems and engineering
- when_to_use: Shortcuts may compound into future drag.
- diagnostic_question: What future work are we silently borrowing from?
- what_it_changes: Converts shortcuts into explicit debt with interest and owner.
- failure_mode: Using debt language to block useful speed.
- evidence_to_seek: Debt item, interest cost, failure risk, owner, and payoff trigger.
- pairs_with: M046, M092, M100

## M055 - Confirmation bias
- id: M055
- name: Confirmation bias
- family: Psychology and bias
- when_to_use: Evidence is being gathered after a preferred answer emerges.
- diagnostic_question: What would we look for if we wanted to disprove ourselves?
- what_it_changes: Forces disconfirming evidence into the process.
- failure_mode: Token dissent that cannot change the decision.
- evidence_to_seek: Disconfirming tests, ignored evidence, and decision change threshold.
- pairs_with: M002, M007, M098

## M056 - Availability
- id: M056
- name: Availability
- family: Psychology and bias
- when_to_use: Recent, vivid, or loud examples dominate judgment.
- diagnostic_question: Is this important or just easy to remember?
- what_it_changes: Rebalances anecdotes with base rates and denominator data.
- failure_mode: Dismissing true signals because they are vivid.
- evidence_to_seek: Frequency data, recency effects, denominator, and competing examples.
- pairs_with: M013, M021, M057

## M057 - Anchoring
- id: M057
- name: Anchoring
- family: Psychology and bias
- when_to_use: A first number, frame, or proposal may be pulling estimates.
- diagnostic_question: What would we estimate if we had not seen the anchor?
- what_it_changes: Creates independent estimates before negotiating or planning.
- failure_mode: Adjusting from the anchor while believing the estimate is independent.
- evidence_to_seek: Blind estimates, alternative anchors, reference class, and rationale.
- pairs_with: M012, M026, M068

## M058 - Social proof
- id: M058
- name: Social proof
- family: Psychology and bias
- when_to_use: Popularity or consensus is treated as quality.
- diagnostic_question: Are people copying each other or independently validating this?
- what_it_changes: Separates herd behavior from real evidence.
- failure_mode: Rejecting consensus even when it contains distributed knowledge.
- evidence_to_seek: Independent sources, adoption reasons, failed adopters, and expertise quality.
- pairs_with: M021, M059, M088

## M059 - Authority bias
- id: M059
- name: Authority bias
- family: Psychology and bias
- when_to_use: A high-status person or institution influences belief.
- diagnostic_question: Would this claim survive without the authority label?
- what_it_changes: Moves confidence from status to evidence.
- failure_mode: Reflexively opposing authority instead of checking its domain competence.
- evidence_to_seek: Authority's track record, domain fit, evidence, and dissenting experts.
- pairs_with: M003, M055, M058

## M060 - Consistency/commitment
- id: M060
- name: Consistency/commitment
- family: Psychology and bias
- when_to_use: Prior public positions may distort current judgment.
- diagnostic_question: Are we protecting a past commitment or the current goal?
- what_it_changes: Opens the door to revise commitments when facts change.
- failure_mode: Treating flexibility as lack of principle.
- evidence_to_seek: Prior commitments, new evidence, identity stakes, and revision cost.
- pairs_with: M074, M075, M098

## M061 - Liking/disliking
- id: M061
- name: Liking/disliking
- family: Psychology and bias
- when_to_use: Feelings toward a person, brand, or group color evaluation.
- diagnostic_question: Would I judge the same evidence differently from someone I dislike?
- what_it_changes: Separates affect from evidence quality.
- failure_mode: Pretending emotion is absent instead of controlling for it.
- evidence_to_seek: Blind review, swapped identity test, evidence table, and counterexamples.
- pairs_with: M059, M062, M068

## M062 - Envy/jealousy
- id: M062
- name: Envy/jealousy
- family: Psychology and bias
- when_to_use: Status comparison may drive a decision.
- diagnostic_question: Would this still matter if nobody could compare status?
- what_it_changes: Removes status pain from strategic analysis.
- failure_mode: Calling all ambition envy.
- evidence_to_seek: Status trigger, practical value, emotional residue, and opportunity cost.
- pairs_with: M004, M071, M081

## M063 - Denial
- id: M063
- name: Denial
- family: Psychology and bias
- when_to_use: Evidence threatens identity, comfort, or sunk plans.
- diagnostic_question: What fact are we avoiding because it would force action?
- what_it_changes: Identifies emotionally protected assumptions.
- failure_mode: Accusing others of denial while ignoring your own incentives.
- evidence_to_seek: Avoided metrics, repeated surprises, defensive reactions, and unresolved facts.
- pairs_with: M055, M075, M098

## M064 - Incentive-caused bias
- id: M064
- name: Incentive-caused bias
- family: Psychology and bias
- when_to_use: Someone's judgment may be warped by their reward structure.
- diagnostic_question: What does this person get for believing or saying this?
- what_it_changes: Downgrades testimony where incentives are misaligned.
- failure_mode: Assuming incentives make every statement false.
- evidence_to_seek: Compensation, status, role pressure, conflicts, and independent verification.
- pairs_with: M027, M028, M059

## M065 - Loss aversion
- id: M065
- name: Loss aversion
- family: Psychology and bias
- when_to_use: Avoiding loss may dominate equivalent gain.
- diagnostic_question: Are we overpaying to avoid a visible loss?
- what_it_changes: Reframes the choice around expected value and acceptable downside.
- failure_mode: Ignoring real ruin risk by calling it loss aversion.
- evidence_to_seek: Loss size, gain size, probability, emotional intensity, and survival threshold.
- pairs_with: M015, M005, M066

## M066 - Status quo bias
- id: M066
- name: Status quo bias
- family: Psychology and bias
- when_to_use: Doing nothing is treated as neutral.
- diagnostic_question: If we were not already doing this, would we choose it now?
- what_it_changes: Makes inaction carry explicit cost and risk.
- failure_mode: Forcing change just to avoid inertia.
- evidence_to_seek: Current-state cost, change cost, switching risk, and default beneficiary.
- pairs_with: M004, M050, M075

## M067 - Overconfidence
- id: M067
- name: Overconfidence
- family: Psychology and bias
- when_to_use: Confidence is high despite uncertainty, novelty, or weak feedback.
- diagnostic_question: What probability would an honest outsider assign?
- what_it_changes: Adds calibration, margin of safety, and smaller bets.
- failure_mode: Using humility language while keeping the same risky plan.
- evidence_to_seek: Forecast history, confidence intervals, outside view, and miss cost.
- pairs_with: M005, M012, M026

## M068 - Narrative bias
- id: M068
- name: Narrative bias
- family: Psychology and bias
- when_to_use: A coherent story may be replacing causal proof.
- diagnostic_question: What facts would remain if the story were removed?
- what_it_changes: Separates explanation fluency from causal evidence.
- failure_mode: Rejecting useful narratives that organize real evidence.
- evidence_to_seek: Causal links, missing facts, alternative stories, and predictive tests.
- pairs_with: M006, M008, M055

## M069 - Reciprocation
- id: M069
- name: Reciprocation
- family: Psychology and bias
- when_to_use: Gifts, favors, or concessions may create obligation.
- diagnostic_question: Are we agreeing because value is real or because obligation was triggered?
- what_it_changes: Exposes hidden pressure in negotiations and relationships.
- failure_mode: Treating all reciprocity as manipulation.
- evidence_to_seek: Prior favors, concession sequence, independent value, and exit comfort.
- pairs_with: M027, M039, M061

## M070 - Contrast effect
- id: M070
- name: Contrast effect
- family: Psychology and bias
- when_to_use: Evaluation follows a strong comparison point.
- diagnostic_question: Does this look good only because the previous option was worse?
- what_it_changes: Forces absolute standards instead of relative reactions.
- failure_mode: Ignoring that comparison can reveal real preference.
- evidence_to_seek: Absolute criteria, reordered comparisons, blind review, and baseline options.
- pairs_with: M057, M010, M098

## M071 - Deprivation superreaction
- id: M071
- name: Deprivation superreaction
- family: Psychology and bias
- when_to_use: A threatened loss of freedom, status, access, or benefit creates overreaction.
- diagnostic_question: Is intensity coming from lost entitlement rather than true value?
- what_it_changes: Predicts backlash when taking something away.
- failure_mode: Dismissing legitimate harm as overreaction.
- evidence_to_seek: Prior entitlement, removal timing, affected group, and replacement path.
- pairs_with: M065, M066, M083

## M072 - Stress influence
- id: M072
- name: Stress influence
- family: Psychology and bias
- when_to_use: People decide under fatigue, fear, urgency, or overload.
- diagnostic_question: Would this judgment survive calmer conditions?
- what_it_changes: Adds delay, simplification, or guardrails for stressed decisions.
- failure_mode: Waiting for perfect calm when the decision is time-sensitive.
- evidence_to_seek: Stressors, error rate, time pressure, recovery window, and guardrails.
- pairs_with: M067, M098, M100

## M073 - Pavlovian association
- id: M073
- name: Pavlovian association
- family: Psychology and bias
- when_to_use: A stimulus may trigger automatic liking, fear, or action.
- diagnostic_question: What association is being triggered before reasoning starts?
- what_it_changes: Separates conditioned response from current evidence.
- failure_mode: Over-psychologizing simple preferences.
- evidence_to_seek: Trigger stimulus, repeated pairing, automatic reaction, and changed-context test.
- pairs_with: M061, M068, M070

## M074 - First-conclusion bias
- id: M074
- name: First-conclusion bias
- family: Psychology and bias
- when_to_use: The first plausible answer becomes sticky.
- diagnostic_question: What would be our second and third best explanations?
- what_it_changes: Forces competing hypotheses before commitment hardens.
- failure_mode: Producing token alternatives that cannot win.
- evidence_to_seek: Alternative hypotheses, evidence for each, and decision criteria.
- pairs_with: M055, M014, M060

## M075 - Sunk cost
- id: M075
- name: Sunk cost
- family: Psychology and bias
- when_to_use: Past investment is used to justify continuing.
- diagnostic_question: Would we start this today from zero?
- what_it_changes: Moves decision from past cost to future expected value.
- failure_mode: Ignoring reputation, learning, or transition cost that affects the future.
- evidence_to_seek: Remaining cost, expected future value, exit cost, and alternative use.
- pairs_with: M004, M065, M066

## M076 - Psychological misjudgment from lollapalooza effects
- id: M076
- name: Psychological misjudgment from lollapalooza effects
- family: Psychology and bias
- when_to_use: Several biases or incentives combine into extreme behavior.
- diagnostic_question: Which forces are reinforcing each other at the same time?
- what_it_changes: Explains nonlinear misjudgment instead of blaming one cause.
- failure_mode: Listing many biases without showing reinforcement.
- evidence_to_seek: Combined incentives, social proof, authority, scarcity, commitment, and feedback.
- pairs_with: M027, M058, M064

## M077 - Adaptation
- id: M077
- name: Adaptation
- family: Biology and evolution
- when_to_use: Organisms, users, teams, or competitors change after pressure.
- diagnostic_question: How will the system adapt once this pressure exists?
- what_it_changes: Treats behavior as dynamic rather than fixed.
- failure_mode: Assuming every adaptation is beneficial.
- evidence_to_seek: Pressure, adaptation path, time scale, and unintended traits selected.
- pairs_with: M039, M083, M092

## M078 - Natural selection
- id: M078
- name: Natural selection
- family: Biology and evolution
- when_to_use: Many variants compete under a selection environment.
- diagnostic_question: What traits does this environment reward?
- what_it_changes: Explains which behaviors or products survive regardless of stated ideals.
- failure_mode: Using evolution metaphors without identifying selection pressure.
- evidence_to_seek: Variation, selection criteria, reproduction mechanism, and survival data.
- pairs_with: M027, M047, M084

## M079 - Ecosystem niches
- id: M079
- name: Ecosystem niches
- family: Biology and evolution
- when_to_use: A strategy depends on occupying a specific role in a larger system.
- diagnostic_question: What niche can this occupy better than alternatives?
- what_it_changes: Finds viable positions instead of generic competition.
- failure_mode: Choosing a niche too small or too easy to invade.
- evidence_to_seek: Niche definition, resource flow, competitors, substitutes, and defensibility.
- pairs_with: M030, M076, M080

## M080 - Competition/cooperation
- id: M080
- name: Competition/cooperation
- family: Biology and evolution
- when_to_use: Actors may either fight, coordinate, or symbiose.
- diagnostic_question: Is value higher through rivalry, coordination, or mutualism?
- what_it_changes: Expands strategy beyond win/lose framing.
- failure_mode: Cooperating where incentives make defection dominant.
- evidence_to_seek: Shared surplus, trust mechanism, defection payoff, and repeated interaction.
- pairs_with: M039, M083, M096

## M081 - Signaling
- id: M081
- name: Signaling
- family: Biology and evolution
- when_to_use: Behavior may exist to communicate quality, status, safety, or intent.
- diagnostic_question: What signal is being sent, and is it costly enough to trust?
- what_it_changes: Distinguishes direct utility from communication value.
- failure_mode: Treating every action as mere signaling.
- evidence_to_seek: Audience, signal cost, alternative signals, and observed response.
- pairs_with: M062, M088, M099

## M082 - Homeostasis
- id: M082
- name: Homeostasis
- family: Biology and evolution
- when_to_use: Systems resist change to maintain a stable range.
- diagnostic_question: What mechanism pulls the system back after disruption?
- what_it_changes: Identifies balancing forces that neutralize interventions.
- failure_mode: Treating resistance as irrational instead of stabilizing.
- evidence_to_seek: Set point, feedback mechanism, compensation behavior, and change threshold.
- pairs_with: M041, M044, M066

## M083 - Energy conservation
- id: M083
- name: Energy conservation
- family: Biology and evolution
- when_to_use: A process asks people or systems to spend sustained effort.
- diagnostic_question: Where will effort naturally be conserved or avoided?
- what_it_changes: Designs for lower-friction behavior and realistic maintenance energy.
- failure_mode: Calling people lazy when the system is energy-expensive.
- evidence_to_seek: Effort cost, default path, friction points, and sustained-use evidence.
- pairs_with: M046, M097, M092

## M084 - Evolutionary mismatch
- id: M084
- name: Evolutionary mismatch
- family: Biology and evolution
- when_to_use: Human instincts face modern environments they were not tuned for.
- diagnostic_question: Is an old instinct misfiring in a new context?
- what_it_changes: Explains predictable misbehavior without moralizing it.
- failure_mode: Reducing all behavior to evolution and ignoring local incentives.
- evidence_to_seek: Trigger, ancestral usefulness, modern mismatch, and design countermeasure.
- pairs_with: M056, M072, M096

## M085 - Moat
- id: M085
- name: Moat
- family: Strategy and competition
- when_to_use: Advantage must survive competition.
- diagnostic_question: What prevents capable rivals from copying or eroding this?
- what_it_changes: Tests whether advantage is durable or temporary.
- failure_mode: Calling any strength a moat.
- evidence_to_seek: Copy cost, switching cost, network effects, brand trust, data, and regulation.
- pairs_with: M036, M037, M079

## M086 - Positioning
- id: M086
- name: Positioning
- family: Strategy and competition
- when_to_use: Perception and category choice affect adoption.
- diagnostic_question: What category are we competing in, and why would we be chosen there?
- what_it_changes: Changes the comparison set and buyer criteria.
- failure_mode: Choosing a clever position the audience does not understand.
- evidence_to_seek: Target segment, alternatives, category language, and decision criteria.
- pairs_with: M079, M081, M088

## M087 - Asymmetric payoff
- id: M087
- name: Asymmetric payoff
- family: Strategy and competition
- when_to_use: Downside and upside are uneven.
- diagnostic_question: Is the upside large relative to the capped downside?
- what_it_changes: Finds bets where being wrong is cheap and being right matters.
- failure_mode: Ignoring probability and calling any big upside attractive.
- evidence_to_seek: Downside cap, upside range, probability, reversibility, and time cost.
- pairs_with: M015, M079, M088

## M088 - Optionality
- id: M088
- name: Optionality
- family: Strategy and competition
- when_to_use: Uncertainty is high and future information has value.
- diagnostic_question: Which move keeps valuable future paths open?
- what_it_changes: Prefers reversible probes before irreversible commitments.
- failure_mode: Hoarding options and never exercising them.
- evidence_to_seek: Option value, expiration, carrying cost, trigger to exercise, and downside.
- pairs_with: M025, M050, M087

## M089 - Barbell strategy
- id: M089
- name: Barbell strategy
- family: Strategy and competition
- when_to_use: Combining safety with high-upside experiments beats medium-risk exposure.
- diagnostic_question: Can we protect the base while taking small convex bets?
- what_it_changes: Separates survival from exploration.
- failure_mode: Letting speculative bets quietly consume the safe base.
- evidence_to_seek: Safe core, experiment budget, capped downside, upside trigger, and review cadence.
- pairs_with: M005, M087, M088

## M090 - Specialization
- id: M090
- name: Specialization
- family: Strategy and competition
- when_to_use: Focus may create advantage through depth.
- diagnostic_question: What should we become unusually good at, and what should we stop doing?
- what_it_changes: Trades breadth for compounding skill and reputation.
- failure_mode: Overspecializing in a shrinking or irrelevant niche.
- evidence_to_seek: Skill compounding, market need, opportunity cost, and adjacent flexibility.
- pairs_with: M029, M079, M092

## M091 - Cooperation vs defection
- id: M091
- name: Cooperation vs defection
- family: Strategy and competition
- when_to_use: Repeated interaction creates trust or exploitation risk.
- diagnostic_question: What makes cooperation stable against defection?
- what_it_changes: Designs trust, enforcement, and exit rules.
- failure_mode: Trusting goodwill when defection has high payoff and low penalty.
- evidence_to_seek: Repetition, visibility, penalties, reputation, and fallback options.
- pairs_with: M039, M080, M096

## M092 - Winner-take-most dynamics
- id: M092
- name: Winner-take-most dynamics
- family: Strategy and competition
- when_to_use: Outcomes may concentrate in a few players, channels, or artifacts.
- diagnostic_question: Does advantage compound toward the leader?
- what_it_changes: Changes whether to pursue broad participation or focused dominance.
- failure_mode: Assuming every market has winner-take-most dynamics.
- evidence_to_seek: Network effects, scale advantage, distribution concentration, and multi-homing.
- pairs_with: M036, M085, M023

## M093 - Deliberate practice
- id: M093
- name: Deliberate practice
- family: Learning, execution, and organizations
- when_to_use: Skill improvement matters more than raw activity.
- diagnostic_question: Is practice targeted, feedback-rich, and slightly beyond current ability?
- what_it_changes: Converts repetition into designed skill acquisition.
- failure_mode: Confusing hours spent with deliberate practice.
- evidence_to_seek: Target skill, feedback loop, difficulty level, repetition count, and correction.
- pairs_with: M098, M099, M023

## M094 - Feedback quality
- id: M094
- name: Feedback quality
- family: Learning, execution, and organizations
- when_to_use: Learning or control depends on signals from reality.
- diagnostic_question: Is feedback timely, specific, accurate, and tied to the goal?
- what_it_changes: Improves the signal before optimizing behavior.
- failure_mode: Treating noisy metrics as truth.
- evidence_to_seek: Feedback delay, accuracy, specificity, noise, and link to final outcome.
- pairs_with: M041, M053, M098

## M095 - Checklists
- id: M095
- name: Checklists
- family: Learning, execution, and organizations
- when_to_use: Repeated execution can fail through omission.
- diagnostic_question: Which critical steps must never rely on memory?
- what_it_changes: Makes recurring quality enforceable and inspectable.
- failure_mode: Creating long checklists nobody uses.
- evidence_to_seek: Critical steps, failure history, checklist length, owner, and use proof.
- pairs_with: M100, M045, M054

## M096 - Trust
- id: M096
- name: Trust
- family: Learning, execution, and organizations
- when_to_use: Coordination requires relying on another actor.
- diagnostic_question: What evidence makes reliance justified?
- what_it_changes: Turns trust from feeling into evidence, incentives, and history.
- failure_mode: Replacing trust with paperwork that does not change behavior.
- evidence_to_seek: Track record, incentive alignment, transparency, recovery behavior, and auditability.
- pairs_with: M028, M091, M100

## M097 - Culture as repeated behavior
- id: M097
- name: Culture as repeated behavior
- family: Learning, execution, and organizations
- when_to_use: Norms matter more than written rules.
- diagnostic_question: What behavior gets repeated, copied, and tolerated?
- what_it_changes: Evaluates culture from actions and reinforcement, not slogans.
- failure_mode: Treating a document as culture.
- evidence_to_seek: Repeated behaviors, rewarded examples, tolerated violations, and onboarding signals.
- pairs_with: M027, M048, M100

## M098 - Coordination cost
- id: M098
- name: Coordination cost
- family: Learning, execution, and organizations
- when_to_use: Multiple people, agents, tools, or teams must work together.
- diagnostic_question: How much energy is spent aligning work instead of doing it?
- what_it_changes: Prices handoffs, shared context, meetings, and state synchronization.
- failure_mode: Ignoring coordination until execution slows down.
- evidence_to_seek: Handoffs, communication paths, wait time, context loss, and ownership clarity.
- pairs_with: M033, M035, M052

## M099 - Goodhart's law
- id: M099
- name: Goodhart's law
- family: Learning, execution, and organizations
- when_to_use: A metric becomes a target.
- diagnostic_question: How will this metric be gamed once people optimize for it?
- what_it_changes: Adds anti-gaming checks and outcome safeguards.
- failure_mode: Rejecting all metrics because metrics can be gamed.
- evidence_to_seek: Metric definition, gaming paths, proxy gap, audit signal, and counter-metric.
- pairs_with: M027, M048, M094

## M100 - Accountability
- id: M100
- name: Accountability
- family: Learning, execution, and organizations
- when_to_use: Work can drift without ownership, proof, or consequence.
- diagnostic_question: Who owns the result, what proof is required, and what happens if it fails?
- what_it_changes: Makes responsibility inspectable and enforceable.
- failure_mode: Naming an owner without authority or evidence requirements.
- evidence_to_seek: Owner, authority, acceptance criteria, evidence path, review cadence, and consequence.
- pairs_with: M028, M095, M097
