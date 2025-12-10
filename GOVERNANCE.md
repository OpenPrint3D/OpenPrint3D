# OpenPrint3D Governance & Decision Policy

OpenPrint3D is an open-source, community-driven project. Its long-term success depends on transparent collaboration, clear responsibilities, and respectful interaction. This document defines how decisions are made, how contributors become maintainers, and how community spaces are used.

---

## 1. Guiding Principles

OpenPrint3D is founded on the following core principles:

- **Transparency** — All project-affecting decisions must be publicly visible and documented.
- **Neutrality** — No single vendor, organization, or individual should dominate the project.
- **Inclusivity** — Contributors of all backgrounds and skill levels are welcome.
- **Stability** — Standards, schemas, and APIs evolve through structured proposals, not unilateral action.
- **Openness** — The community is encouraged to participate meaningfully in shaping the direction of the project.

---

## 2. Roles and Responsibilities

### Contributors
Anyone who files issues, submits pull requests, writes documentation, or provides constructive feedback is a contributor. No special permissions are required.

### Provisional Maintainers
Provisional Maintainers are contributors who have demonstrated initiative, sound judgment, and alignment with the project’s goals. They may receive elevated permissions (e.g., issue triage, PR reviews) at the discretion of the Project Lead.

The purpose of provisional status is to:
- Onboard new maintainers,
- Evaluate long-term fit,
- Distribute workload early without conferring full authority.

### Maintainers
Maintainers are trusted, long-term contributors who consistently participate, demonstrate technical depth, and uphold project values.

Maintainers are responsible for:
- Reviewing and merging PRs,
- Participating in technical discussions,
- Helping shape and execute the roadmap,
- Upholding the Code of Conduct,
- Supporting a healthy contributor ecosystem.

Promotion from Provisional Maintainer to Maintainer is determined by the Project Lead, with input from existing maintainers.

### Project Lead
The Project Lead:
- Provides overall project direction,
- Ensures adherence to governance,
- Mediates disputes,
- Adds or removes maintainers when necessary,
- Makes final decisions when consensus cannot be reached.

The Project Lead does not override community process except when required for project stability.

---

## 3. Decision Making

### Lazy Consensus

OpenPrint3D uses a **lazy consensus** model for most decisions:

- A proposal (issue, PR, or RFC) is considered accepted if **no Maintainer raises a substantive objection within a reasonable time**, typically **72 hours**.
- Silence is interpreted as agreement.
- If concerns are raised, the proposer and maintainers collaborate to revise the proposal.
- If consensus cannot be reached after good-faith effort, the matter is escalated to the Project Lead for a final decision.

Lazy consensus keeps the project agile while ensuring maintainers have the opportunity to participate.

### Consensus First

Whenever possible, decisions should be made through open discussion and rough consensus among maintainers.

### When Consensus Cannot Be Reached

If a proposal becomes contentious or blocked:
1. Maintainers discuss in the GitHub issue/PR/RFC.
2. If disagreement persists, the Project Lead mediates.
3. The Project Lead makes the final decision.
4. The decision is documented publicly.

### Changes to Governance

Modifications to this governance document must:
- Be proposed via a GitHub pull request,
- Undergo community review,
- Be approved by the Project Lead.

---

## 4. Communication Channels

To ensure transparency, longevity, and equal access, **GitHub is the authoritative communication platform for OpenPrint3D.**

### 4.1 Authoritative Project Communication

All official project matters must occur on GitHub, including:

- Technical proposals  
- Issues and bug reports  
- Pull requests  
- RFCs  
- Governance discussions  
- Standards documentation  
- Final decisions or votes  

GitHub acts as the **source of truth** due to its:
- Public visibility  
- Permanent record  
- Searchability  
- Open participation  
- Clear history of decisions  

No project decision may be finalized on Discord, private chats, or any other platform without formal documentation on GitHub.

### 4.2 Community Spaces (Discord, etc.)

Real-time platforms such as Discord are welcomed and may host:

- Community support chats  
- Maintainer coordination  
- Brainstorming sessions  
- Live discussions  
- Office hours  
- Social/community events  

However:

**Discord is not an authoritative decision-making venue.**  
Any idea, agreement, or concern originating on Discord **must** be brought to GitHub as an issue, PR, or RFC before it can influence the project.

Discord may receive GitHub webhook notifications *only if* they reinforce GitHub’s primary role, and only after maintainers reach consensus on their configuration.

---

## 5. Code of Conduct

All contributors, maintainers, and community members must adhere to the OpenPrint3D Code of Conduct, which requires:

- Respectful communication  
- Inclusive behavior  
- Constructive engagement  
- Avoiding personal attacks, harassment, or public shaming  
- No targeted call-outs of individuals or organizations  

Violations will be addressed by the Project Lead and maintainers according to the Code of Conduct.

---

## 6. Resolving Disputes

If disagreements arise:

1. Attempt resolution in the appropriate GitHub thread.  
2. If unresolved, maintainers may request mediation by another maintainer.  
3. Persistent disputes are escalated to the Project Lead.  
4. The Project Lead’s decision is final and will be documented publicly.

---

## 7. Becoming a Maintainer

A contributor may be invited to become a Provisional Maintainer when they:

- Consistently provide high-quality contributions,  
- Understand the project’s goals and architecture,  
- Communicate clearly and respectfully,  
- Demonstrate reliability and initiative.

They may become a full Maintainer when they:

- Maintain steady participation,  
- Show constructive engagement in reviews and discussions,  
- Demonstrate sound technical judgment,  
- Align with the project’s guiding principles.

The Project Lead makes the final determination.

---

## 8. Leaving or Changing Roles

Contributors and maintainers may step down at any time.

The Project Lead may remove or reassign maintainers if they:

- Become inactive for an extended period,  
- Repeatedly violate governance or communication norms,  
- Behave in a manner harmful to the project or community.  

Role changes are documented publicly through a GitHub issue or PR.

---

## 9. Project Infrastructure

Any infrastructure intended to serve as **official project resources** (e.g., Discord integrations, documentation sites, registries, automation, or tooling) must:

- Be proposed and discussed on GitHub,  
- Be approved by the Project Lead,  
- Be transferable to the project if the original creator leaves,  
- Have clear documentation in the repository.  

This ensures sustainability, openness, and continuity.

---

## 10. Final Notes

OpenPrint3D is a community effort with the goal of improving interoperability and standardization across the 3D-printing ecosystem. This governance document is intentionally lightweight at this stage but provides structure to ensure transparency, neutrality, and long-term continuity.

As the project evolves, this document may be refined through open proposals and pull requests.
