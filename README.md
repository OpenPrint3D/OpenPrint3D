# OpenPrint3D — An Open, Slicer-Independent Profile Format

OpenPrint3D is an open proposal for standardizing printer, filament, and process profiles in a simple, neutral JSON format.
It’s designed to make 3D-printing configurations easier to share, easier to maintain, and easier for tools or slicers to import — without replacing or competing with existing slicers.

This project began independently before the announcement of Prusa’s OpenPrintTag, but the two efforts are naturally complementary:
OpenPrintTag focuses on spool/tag metadata, while OpenPrint3D focuses on the configuration layer behind those materials.

The goal is a lightweight, community-driven framework that reduces fragmentation and provides a clean, consistent foundation for anyone building slicer tooling, print-farm systems, material libraries, or automation.

OpenPrint3D is currently an early-stage draft (schema v0.1). Feedback, discussion, and contributions are welcome.

#Community & Discord
We invite you to join the official OpenPrint3D Discord to hang out, ask questions, and come together as a community. The Discord is intended for fun, ease of use, and open discussion among users. https://discord.gg/PDwzze2Bbw

Please Note:
While the Discord is great for brainstorming and community building, all official decisions, standard changes, and technical governance are handled exclusively on GitHub. To ensure transparency and proper tracking, please submit formal proposals, bug reports, and pull requests directly to this repository

# OpenPrint3D Profile Composition

Below is a high-level view of how OpenPrint3D structures configurations.

Each *complete* profile is assembled by combining:

   • A **Printer** definition  
   • A **Filament** definition  
   • A **Process** definition  

These three components map into a slicer's internal configuration model.

<img width="1000" height="900" alt="OpenPrint3D-Diagram-v0 1" src="https://github.com/user-attachments/assets/f6f9280a-e3c2-428d-8c47-41ec3696a725" />

**Key Idea:**  
OpenPrint3D does *not* replace slicers — it provides a clean, neutral, shared
format for describing the *intent* of a printer/filament/process combination.

Slicers can then map these fields into their own internal settings however they choose.
