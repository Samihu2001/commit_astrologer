def get_rules():
    """Returns the classic astrology rules."""
    return {
        "fix": [
            ["Mercury in retrograde suggests you'll spend extra time debugging that semicolon.", "A minor celestial alignment indicates a quick patch, but double-check for unforeseen consequences."],
            ["The cosmic winds favor bug squashing, but be wary of phantom errors that reappear unexpectedly."],
        ],
        "feat": [
            ["A new star is born in the codebase! Its brilliance may temporarily blind those who gaze upon it (expect integration issues).", "The planets align for innovation, but ensure this new feature doesn't disrupt the delicate balance of the system."],
            ["Jupiter's influence brings growth, but also potential bloat. Keep it lean and focused."],
        ],
        "refactor": [
            ["The very fabric of code is being rewoven. Expect some threads to tangle (merge conflicts are likely).", "Saturn's discipline demands a thorough refactoring, but hasty changes could invite chaos."],
            ["Cosmic renovation is underway. While necessary, prepare for unexpected structural quirks to emerge."],
        ],
        "docs": [
            ["The ancient scrolls of documentation are updated. Their wisdom will guide future travelers.", "A well-documented commit shines brightly in the nebula of code."],
            ["Clarity dawns as the documentation evolves. The path ahead becomes less treacherous."],
        ],
        "test": [
            ["Celestial testing reveals a stable configuration. The code is blessed by the algorithmic gods.", "Strong test coverage acts as a cosmic shield against future anomalies."],
            ["The omens are good; the tests pass. However, even the most favorable constellations can hide surprises."],
        ],
        "merge": [
            ["A harmonious convergence of branches is foretold. The cosmic dance of integration proceeds smoothly.", "The gravitational pull of the main branch is strong. Resistance is futile (and unnecessary)."],
            ["Planetary alignment suggests a conflict-free union. Enjoy the peaceful merging of worlds."],
        ],
        "wip": [
            ["The cosmos is still forming this code. Its final shape remains shrouded in mystery.", "A nascent star, full of potential but yet undefined. Expect significant changes."],
            ["Early stages under a new moon. The path forward is uncertain."],
        ],
        "remove": [
            ["A celestial body is extinguished from the codebase. Ensure its gravitational influence is not missed.", "The void left by the removed code may create unexpected ripples."],
            ["Pruning the cosmic tree. Ensure no essential branches are accidentally severed."],
        ],
        "performance": [
            ["The code achieves faster orbital velocity! Beware of exceeding the limits of the system.", "A boost in cosmic energy propels the code forward with greater speed."],
        ],
    }