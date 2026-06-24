#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the dataset for the JPT/SPE Enhanced-Recovery -> Wells Engineering dashboard.

Source: https://jpt.spe.org/topic/enhanced-recovery  (pages 1-12, Nov 2023 - Jun 2026)
Articles are paywalled; only the public brief/abstract is available, so all
technical-summary fields are ABSTRACT-FAITHFUL (low-inference, grounded in the brief).

Outputs: data.json  (consumed by the self-contained dashboard HTML)
"""

import json, re
from datetime import datetime

BASE = "https://jpt.spe.org"

# ----------------------------------------------------------------------------
# RAW RECORDS  (title, slug, source_tag, date, author, abstract, locked)
# ----------------------------------------------------------------------------
R = [
 # ---- 2026 ----
 ("EOR Operations (2026)", "/eor-operations-2026", "Enhanced recovery", "June 1, 2026", "Kristian Mogensen",
  "The industry clearly needs creative solutions that are affordable and operationally flexible, and the three papers selected for this Technology Focus highlight some innovative approaches that aim to unlock those extra barrels.", False),
 ("Novel Gas-/Liquid-Coinjection EOR Process Enters the Permian", "/novel-gas-liquid-coinjection-eor-process-enters-the-permian-restricted", "Enhanced recovery", "June 1, 2026", "",
  "This paper details a new enhanced oil recovery method piloted successfully by several operators in the Bakken and recently implemented in the Midland play of the Permian Basin.", True),
 ("Closed-Loop Completions Program Holds Potential to Transform Hydraulic Fracturing", "/closed-loop-completions-program-holds-potential-to-transform-hydraulic-fracturing-restricted", "Enhanced recovery", "June 1, 2026", "",
  "The paper presents the design and successful field deployment of the first closed-loop hydraulic fracturing program.", True),
 ("Alaska North Slope Fracturing Campaign Provides Best Practices, Better Decisions", "/alaska-north-slope-fracturing-campaign-provides-best-practices-better-decisions-restricted", "Enhanced recovery", "June 1, 2026", "",
  "This paper reviews fracturing-program design, completion technology, real-time data collection, data integration, and lessons learned for the Pikka development on the North Slope of Alaska.", True),
 ("Tool-Free Fishbone Fracture Acidizing Stimulation Implemented in Openhole Horizontal Well", "/tool-free-fishbone-fracture-acidizing-stimulation-implemented-in-openhole-horizontal-well-restricted", "Acidizing/stimulation", "June 1, 2026", "",
  "This paper presents a case study of a tool-free fishbone fracture stimulation technology using sand jetting and acidizing in openhole wells, providing a technical solution for low-permeability and complex-lithology carbonate reservoirs in the Middle East.", True),
 ("Encapsulated Polymer Technology Overcomes Shear Degradation and Injectivity Loss Offshore", "/encapsulated-polymer-technology-overcomes-shear-degradation-and-injectivity-loss-offshore-restricted", "Enhanced recovery", "June 1, 2026", "",
  "This paper describes the use of encapsulated polymer technology to address the issues of shear degradation and injectivity integrity faced in the application of polymer flooding in an offshore development context.", True),
 ("Acid Fracturing and Hydraulic Fracturing Applied in a Single Well for a Deep Carbonate Reservoir", "/acid-fracturing-and-hydraulic-fracturing-applied-in-a-single-well-for-a-deep-carbonate-reservoir-restricted", "Enhanced recovery", "June 1, 2026", "",
  "The paper describes a project in which extremely challenging stimulations were performed in a fractured tight carbonate in a complex strike/slip stress faulting regime with high tectonic stresses.", True),
 ("Test Proves Validity of In-Situ Combustion in the Permian Basin", "/test-proves-validity-of-in-situ-combustion-in-the-permian-basin-restricted", "Enhanced recovery", "June 1, 2026", "",
  "This study provides the first experimental evidence that in-situ combustion is feasible in Permian shale under realistic rock-fluid conditions.", True),
 ("Acidizing (2026)", "/acidizing-2026", "Enhanced recovery", "June 1, 2026", "Chris Carpenter",
  "The works highlighted in this year's Acidizing feature demonstrate novel, diverse innovations in sustainability, enhanced productivity, and logistical efficiency by authors of SPE conference papers.", False),
 ("In Shale, There's No Single Playbook for How To Do EOR", "/in-shale-theres-no-single-playbook-for-how-to-do-eor-restricted", "Enhanced recovery", "June 1, 2026", "Trent Jacobs",
  "New insights from Chevron, Occidental Petroleum, and others at the SPE Improved Oil Recovery Conference highlight the different paths companies are using to squeeze more out of tight rocks.", True),
 ("Pioneers Honored for Advancing Improved Oil Recovery", "/pioneers-honored-for-advancing-improved-oil-recovery", "SPE News", "May 18, 2026", "JPT Staff",
  "Three experts were recognized with the Pioneer Award at the 2026 SPE Improved Oil Recovery Conference in Tulsa for their technological contributions to improved oil recovery.", False),
 ("Inside NETL's Oil and Gas Center of Excellence, an Engagement Hub for US Upstream", "/inside-netls-oil-and-gas-center-of-excellence-an-engagement-hub-for-us-upstream", "R&D/innovation", "May 6, 2026", "Trent Jacobs",
  "Acting director of the new center Ale Hakala outlines the research priorities guiding the newly established center's focus on production enhancement technologies.", False),
 ("AI-Based Technology Enables Real-Time GOR Control in Oil-Rim Reservoir Management", "/ai-based-technology-enables-real-time-gor-control-in-oil-rim-reservoir-management-restricted", "Digital Oil Field", "May 1, 2026", "",
  "The authors write that deployment of artificial-intelligence-based high-gas/oil ratio well-control technology enabled stabilization of well performance and maintenance of optimal production conditions.", True),
 ("Operators Refine Exploration and Development Strategies", "/operators-refine-exploration-and-development-strategies", "Mature fields", "April 9, 2026", "Jennifer Pallanich",
  "Technology and partnerships remain important, while phased approaches may supplant lengthy appraisal programs, experts said during CERAWeek.", False),
 ("Steam-Sensitive Flow-Control Device Implemented in Surmont SAGD Project", "/steam-sensitive-flow-control-device-implemented-in-surmont-sagd-project-restricted", "Unconventional/complex reservoirs", "April 1, 2026", "",
  "This paper introduces a novel steam-sensitive flow-control device designed to restrict the production of steam and low-subcool liquids while allowing higher mobility of oil-phase fluids.", True),
 ("SAGD Performance at Blowdown Phase Optimized With Autonomous Inflow Control Valves", "/sagd-performance-at-blowdown-phase-optimized-with-autonomous-inflow-control-valves-restricted", "Unconventional/complex reservoirs", "April 1, 2026", "",
  "This study integrates laboratory testing with reservoir simulation to evaluate the effectiveness of autonomous inflow-control valves in managing late-life steam-assisted gravity-drainage production challenges.", True),
 ("Heavy Oil (2026)", "/heavy-oil-2026", "Enhanced recovery", "April 1, 2026", "Sahar Ghannadi",
  "Steam-assisted gravity drainage (SAGD) technology continues to advance rapidly, driven by improvements in numerical simulation, inflow-control technologies, fiber-optic monitoring, and real-time production optimization.", False),
 ("Dynamic Gas Separation Integrated Into SAGD for Improved ESP Performance", "/dynamic-gas-separation-integrated-into-sagd-for-improved-esp-performance-restricted", "Unconventional/complex reservoirs", "April 1, 2026", "",
  "This paper demonstrates the effectiveness of integrating dynamic gas separation with existing gas-avoidance methods within the same electrical submersible pump string to address these issues.", True),
 ("Emissions Reduced, Recovery Enhanced From Permeate Stream Using Integrated Process", "/emissions-reduced-recovery-enhanced-from-permeate-stream-using-integrated-process-restricted", "LNG", "April 1, 2026", "",
  "This paper describes the operator's initiative to reduce greenhouse-gas emissions and recover additional hydrocarbon, monetizing it as sales gas, by integrating upstream and downstream gas facilities in a unified approach.", True),
 ("SCCO2/Brine Injection or WAG Couple With Saltwater-Disposal Wells for Carbon Sequestration", "/scco2-brine-injection-or-wag-couple-with-saltwater-disposal-wells-for-carbon-sequestration-restricted", "Decarbonization", "March 1, 2026", "",
  "This paper reviews the simultaneous supercritical CO2/brine aquifer injection and water-alternating-gas methods for geologic carbon sequestration and proposes a novel integration with saltwater-disposal wells.", True),
 ("Enhanced Geothermal System Proppant Stimulation Targets High-Temperature Dry Rock", "/enhanced-geothermal-system-proppant-stimulation-targets-high-temperature-dry-rock-restricted", "Geothermal energy", "March 1, 2026", "",
  "This paper provides an account of the design, implementation, and operational insights from an enhanced geothermal system proppant stimulation targeting a volcanic, dry rock setting with an approximately 330C bottomhole temperature.", True),
 ("Multiagent AI Improves Offshore Production Surveillance and Intervention", "/multiagent-ai-improves-offshore-production-surveillance-and-intervention-restricted", "Well intervention", "March 1, 2026", "",
  "This paper introduces an agentic artificial-intelligence framework designed for offshore production surveillance and intervention.", True),
 ("Record-Breaking Enhanced Geothermal System Designed for Project Cape, Utah", "/record-breaking-enhanced-geothermal-system-designed-for-project-cape-utah-restricted", "Geothermal energy", "March 1, 2026", "",
  "This paper describes modeling work performed to design fracturing treatment and spacing for wells in the Project Cape enhanced geothermal system in Utah.", True),
 ("Saipem Lands Safaniya Trunkline EPCI Order Under Aramco Framework", "/saipem-lands-safaniya-trunkline-epci-order-under-aramco-framework", "Field/project development", "February 27, 2026", "JPT Staff",
  "The award comes as a contract release purchase order under a long-term agreement that simplifies ongoing efforts to maintain mature field production in Saudi Arabia.", False),
 # ---- 2026 Jan / 2025 ----
 ("Rewriting the Artificial Lift Playbook", "/rewriting-the-artificial-lift-playbook-restricted", "Artificial lift", "January 1, 2026", "Jennifer Pallanich",
  "Operators are turning to new gas-lift and nanoparticle-fluid technologies to drive up production rates.", True),
 ("Integrated Well-Network-Design Mode Developed for Carbon-Dioxide EOR and Storage", "/integrated-well-network-design-mode-developed-for-co-eor-and-storage-restricted", "Enhanced recovery", "January 1, 2026", "",
  "This paper addresses the difficulty in adjusting late-stage production in waterflooded reservoirs and proposes an integrated well-network-design mode for carbon-dioxide enhanced oil recovery and storage.", True),
 ("Fast Predictive Models Developed for Carbon-Dioxide EOR and Storage in Mature Oil Fields", "/fast-predictive-models-developed-for-co-eor-and-storage-in-mature-oil-fields-restricted", "Enhanced recovery", "January 1, 2026", "",
  "This work presents the development of fast predictive models and optimization methodologies to evaluate the potential of carbon-dioxide EOR and storage operations quickly in mature oil fields.", True),
 ("Deep-Learning Technique Optimizes Sequestration, Oil Production in CCUS Projects", "/deep-learning-technique-optimizes-sequestration-oil-production-in-ccus-projects-restricted", "Enhanced recovery", "January 1, 2026", "",
  "The authors of this paper apply a deep-learning model for multivariate forecasting of oil production and carbon-dioxide-sequestration efficiency across a range of water-alternating-gas scenarios using field data from six legacy carbon-dioxide enhanced-oil-recovery projects.", True),
 ("EOR Modeling (2026)", "/eor-modeling-2026", "Enhanced recovery", "January 1, 2026", "Luky Hendraningrat",
  "As the industry accelerates carbon capture, use, and storage initiatives, modeling innovations for carbon-dioxide injection and enhanced oil recovery have become critical for optimizing recovery and ensuring secure storage. Recent studies highlight a shift toward data-driven and hybrid approaches that combine computational efficiency with operational practicality.", False),
 ("Microfluidic Strategies Use Ferrofluids for Enhanced Recovery", "/microfluidic-strategies-use-ferrofluids-for-enhanced-recovery-restricted", "Enhanced recovery", "November 1, 2025", "",
  "The objective of this microfluidic investigation is to identify and test two novel applications for magnetic fluids in porous media for subsurface oilfield applications.", True),
 ("Eagle Ford Huff 'n' Puff Single-Well Pilot Uses Large Y-Grade Injection Volumes", "/eagle-ford-huff-n-puff-single-well-pilot-uses-large-y-grade-injection-volumes-restricted", "Enhanced recovery", "November 1, 2025", "",
  "This paper describes a study to design and implement an enhanced oil recovery project via huff 'n' puff using Y-grade injectant.", True),
 ("Huff 'n' Puff for Shale Oil Recovery Uses Surfactants, Nanoparticles, and Ketones", "/huff-n-puff-for-shale-oil-recovery-uses-surfactants-nanoparticles-and-ketones-restricted", "Enhanced recovery", "November 1, 2025", "",
  "This study compares water-based chemicals including surfactants, nanoparticles, and ketones that can be used for enhancing the oil recovery of shale-oil reservoirs.", True),
 ("EOR Operations (2025, Nov)", "/eor-operations-2025-2", "Enhanced recovery", "November 1, 2025", "Hideharu Yonebayashi",
  "Entrepreneurial mindsets with the motivation to explore new materials, not limited to focusing on traditional hydrocarbon gas, carbon dioxide, and chemicals such as polymer and surfactant, are becoming more important for broadening prospects beyond the conventional EOR scene.", False),
 ("Integrated Approach to Gasfield Development, Carbon Sequestration Minimizes Emissions", "/integrated-approach-to-gasfield-development-carbon-sequestration-minimizes-emissions-restricted", "Emission management", "October 1, 2025", "",
  "This study explores the feasibility of implementing in-situ carbon dioxide recycling for sequestration as a fit-for-purpose developmental strategy for a Malaysian gas field characterized by an initial carbon-dioxide content of approximately 60%.", True),
 ("Alternative Carbon Carrier Technology Could Improve Oil Production - and Carbon Storage, Too", "/alternative-carbon-carrier-technology-could-improve-oil-production-and-carbon-storage-too", "Enhanced recovery", "September 9, 2025", "The University of Texas at Austin",
  "In a study that applied alternative carbon carrier technology to enhanced oil recovery (EOR) scenarios, researchers at The University of Texas at Austin found that the new method recovered up to 19.5% more oil and stored up to 17.5% more carbon than conventional EOR methods.", False),
 ("ML-Based Co-Optimization Framework Improves CO2 Sequestration and Oil Recovery", "/ml-based-co-optimization-framework-improves-co-sequestration-and-oil-recovery-restricted", "Decarbonization", "September 1, 2025", "",
  "This paper presents a novel workflow with multiobjective optimization techniques to assess the integration of pressure-management methodologies for permanent geological carbon dioxide storage in saline aquifers.", True),
 ("Structured Project-Management Approach Accelerates Marginal Field Development", "/structured-project-management-approach-accelerates-marginal-field-development-restricted", "Field/project development", "September 1, 2025", "",
  "This paper reviews lean construction management processes adopted in the Apani Field development, from facility design to construction management and drilling-location preparation.", True),
 ("Physics-Informed Machine Learning Enhances Permeability Prediction in Carbonate Reservoirs", "/physics-informed-machine-learning-enhances-permeability-prediction-in-carbonate-reservoirs-restricted", "Reservoir characterization", "August 1, 2025", "",
  "This study integrates physics-based constraints into machine-learning models, thereby improving their predictive accuracy and robustness.", True),
 ("Modeling Tool Developed To Predict Condensate Emulsions", "/modeling-tool-developed-to-predict-condensate-emulsions-restricted", "Enhanced recovery", "August 1, 2025", "",
  "This study presents the development of a novel modeling tool designed to predict condensate emulsions, focusing on key factors causing emulsions such as pH, solid content, asphaltene concentration, droplet size, and organic acids.", True),
 ("Analysis, Skin Calculation With Dual-Method Stimulation Enhances Gas Production", "/analysis-skin-calculation-with-dual-method-stimulation-enhances-gas-production-restricted", "Enhanced recovery", "August 1, 2025", "",
  "This study explores enhancing gas production through a novel combination of prestimulation using a coiled tubing unit and high-rate matrix acidizing.", True),
 ("Physics-Inspired Data-Driven Method Manages Liquid Loading", "/physics-inspired-data-driven-method-manages-liquid-loading-restricted", "Enhanced recovery", "August 1, 2025", "",
  "This work introduces a fast, methodical approach to detect liquid loading using easily available field data while avoiding traditional assumptions and to determine critical gas rates directly from field data.", True),
 ("Effect of Salinity and Hardness on Hydrolyzed Polyacrylamide Rheology in Sandstone", "/effect-of-salinity-and-hardness-on-hydrolyzed-polyacrylamide-rheology-in-sandstone", "Enhanced recovery", "July 16, 2025", "SPE Journal",
  "This paper studies the effect of salinity and hardness on partially hydrolyzed polyacrylamide rheology in sandstones with relevance to polymer flooding models and simulations.", False),
 ("Completion and Reservoir Data Deciphers Productivity Drivers in Unconventional Plays", "/completion-and-reservoir-data-deciphers-productivity-drivers-in-unconventional-plays-restricted", "Unconventional/complex reservoirs", "July 1, 2025", "",
  "This study aims to thoroughly assess the influence of various completions, fracturing stimulation, and intrinsic reservoir properties affecting the productivity of 10 major unconventional plays while uncovering insights and trends unique to each play.", True),
 ("Workflow Improves Assessment of Permeability in Tight Rock Samples", "/workflow-improves-assessment-of-permeability-in-tight-rock-samples-restricted", "Unconventional/complex reservoirs", "July 1, 2025", "",
  "This paper introduces new methods to perform reliable permeability and saturation-dependent relative permeability measurements in organic-rich mudrock core samples using a pressure-decay setup.", True),
 ("Field Study Explores Condensate-Banking Effect in Unconventional Gas-Condensate Reservoir", "/field-study-explores-condensate-banking-effect-in-unconventional-gas-condensate-reservoir-restricted", "Unconventional/complex reservoirs", "July 1, 2025", "",
  "This paper investigates condensate-banking effects on well performance by conducting field-modeling studies on Delaware Basin deep Wolfcamp condensate producers using compositional simulation models with hydraulic fractures.", True),
 ("URTeC: Untapped Potential: Enhanced Recovery Could Keep Shale Plays Producing", "/urtec-untapped-potential-enhanced-recovery-could-keep-shale-plays-producing", "Enhanced recovery", "June 13, 2025", "Jennifer Pallanich",
  "Secondary and tertiary efforts are critical for sustaining the productive lives of unconventional plays.", False),
 ("EOR Operations (2025)", "/eor-operations-2025", "Enhanced recovery", "June 1, 2025", "Kristian Mogensen",
  "The three papers selected for this feature highlight some creative solutions that aim to increase project value by either increasing recovery or optimizing injectant cost, or both.", False),
 ("Review Investigates Selection of Viscosities for Injected Polymers", "/review-investigates-selection-of-viscosities-for-injected-polymers-restricted", "Enhanced recovery", "June 1, 2025", "",
  "This paper discusses the effect of injected-polymer viscosity on various aspects of a project, from recovery to surface facilities, including both theoretical arguments and practical field experience-which do not always align.", True),
 ("Multivariate Geochemical Fingerprinting Reveals Effects of EOR Processes", "/multivariate-geochemical-fingerprinting-reveals-effects-of-eor-processes-restricted", "Enhanced recovery", "June 1, 2025", "",
  "This study leverages oil-fingerprinting technology and geochemical data to evaluate the fluid connectivity between a main field and its stepout wells.", True),
 ("Study Using Multifunctional Biosurfactants Offers Insight Into Bakken EOR", "/study-using-multifunctional-biosurfactants-offers-insight-into-bakken-eor-restricted", "Enhanced recovery", "June 1, 2025", "",
  "This paper provides details of a pilot study conducted on multiple wells, showcasing the potential of a novel biotechnology in Bakken enhanced oil recovery.", True),
 ("Targeted Acid-Stimulation Technique Enhances Production in the Montney", "/targeted-acid-stimulation-technique-enhances-production-in-the-montney-restricted", "Acidizing/stimulation", "June 1, 2025", "",
  "The authors of this paper describe a method of stimulating a multizone hydrocarbon-producing well wherein a tool is deployed downhole by wireline to generate acid vapor at a target depth, allowing each interval to be treated uniquely.", True),
 ("Approach Interprets Fracture Growth Through Microseismic Quiescent Zones", "/approach-interprets-fracture-growth-through-microseismic-quiescent-zones-restricted", "Enhanced recovery", "June 1, 2025", "",
  "In this work, microseismic observations are integrated with strain and other observations to investigate the microseismic response in relation to the underlying hydraulic fracture geometry for different rock types.", True),
 ("Acidizing (2025)", "/acidizing-2025", "Enhanced recovery", "June 1, 2025", "Chris Carpenter",
  "This year's Acidizing feature presents three SPE conference papers that discuss an important battlefront of enhanced production-carbonate reservoirs, those plays whose heterogeneity, reactivity, and flow behavior pose challenges that remain comparatively little-understood, despite the industry's intensified efforts to maximize their output.", False),
 ("Study Investigates Effect of Fracture and Vug Networks on Acid-Stimulation Process", "/study-investigates-effect-of-fracture-and-vug-networks-on-acid-stimulation-process-restricted", "Acidizing/stimulation", "June 1, 2025", "",
  "This paper extends an integrated two-scale continuum model that contemplates mass, momentum, and energy changes to study the acid-stimulation process in complex carbonate acid-stimulation systems with the development of fracture and vug networks.", True),
 ("Autonomous Flow-Control Devices Optimize Matrix Acid Stimulation", "/autonomous-flow-control-devices-optimize-matrix-acid-stimulation-restricted", "Acidizing/stimulation", "June 1, 2025", "",
  "The authors of this paper write that autonomous outflow-control devices can positively affect matrix acidizing by providing the best possible conformance.", True),
 ("ATBS Polymer Injectivity in 22-86 md Carbonate Cores", "/atbs-polymer-injectivity-in-22-86-md-carbonate-cores-effects-of-polymer-filtration-mechanical-shearing-and-oil-presence", "Enhanced recovery", "May 23, 2025", "SPE Journal",
  "This study combines preshear degradation, permeability, and oil presence effects to evaluate and improve polymer injectivity using acrylamido tertiary butyl sulfonate (ATBS) polymer in carbonate rock.", False),
 ("Reservoir-Fluid Geodynamics Enable Insights Into Reservoir Connectivity", "/reservoir-fluid-geodynamics-enable-insights-into-reservoir-connectivity-restricted", "Reservoir characterization", "May 1, 2025", "",
  "The authors of this paper describe reservoir-fluid-geodynamics processes that explain the reasons behind varying oil compositions and properties within and across different reservoir compartments.", True),
 ("Robust Integrated Approach Evaluates Heavy Sludge Formation", "/robust-integrated-approach-evaluates-heavy-sludge-formation-restricted", "Unconventional/complex reservoirs", "April 1, 2025", "",
  "This work investigates the root cause of strong oil/water emulsion and if sludge formation is occurring within the reservoir using a robust integrated approach.", True),
 ("Equation of State Models Phase Behavior of Systems Under Reservoir Conditions", "/equation-of-state-models-phase-behavior-of-systems-under-reservoir-conditions-restricted", "Unconventional/complex reservoirs", "April 1, 2025", "",
  "In this work, a perturbed-chain statistical associating fluid theory equation of state has been developed to characterize heavy-oil-associated systems containing polar components and nonpolar components with respect to phase behavior and physical properties.", True),
 ("Subsurface Safety Valves Prevent Self-Flow in Steam-Injection Wells in Heavy Oil Field", "/subsurface-safety-valves-prevent-self-flow-in-steam-injection-wells-in-heavy-oil-field-restricted", "Unconventional/complex reservoirs", "April 1, 2025", "",
  "This paper aims to present thoroughly the application of subsurface safety injection valves in extremely high-temperature environments.", True),
 ("Geothermal Exploitation Achieved by Injection of Supercritical CO2 Into Deep Heavy Oil", "/geothermal-exploitation-achieved-by-injection-of-supercritical-co2-into-deep-heavy-oil-restricted", "Sustainability", "March 1, 2025", "",
  "This paper presents a comprehensive model of geothermal exploitation for depleted deep heavy oil reservoirs through supercritical CO2 injection.", True),
 ("BP Signs Deal To Rehab Iraq's Kirkuk Oil Assets, Boost Production", "/bp-signs-deal-to-rehab-iraqs-kirkuk-oil-assets-boost-production", "Asset/portfolio management", "February 26, 2025", "Pat Davis Szymczak",
  "In a deal described as possibly one of the most important transactions BP has done in 20 years by CEO Murray Auchincloss, the company has agreed contractual terms with the Iraqi government to invest in drilling and infrastructure to rehabilitate and boost production at the Kirkuk oil field.", False),
 ("Experimental Investigation of Factors Affecting Oil Recovery and Displacement Efficiency of CO2 Injection in Carbonate Reservoirs", "/experimental-investigation-of-factors-affecting-oil-recovery-and-displacement-efficiency-of-carbon-dioxide-injection-in-carbonate-reservoirs", "Enhanced recovery", "February 20, 2025", "SPE Journal",
  "Investigation into the parameters affecting the displacement efficiency of CO2 injection under miscible and near-miscible conditions in the presence and absence of mobile water saturation using carbon dioxide core injection experiments.", False),
 ("EOR Modeling (2025)", "/eor-modeling-2025", "Enhanced recovery", "January 1, 2025", "Luky Hendraningrat",
  "CO2 enhanced oil recovery (EOR) provides an attractive and commercially established technique to store CO2 underground. EOR modeling is crucial because complex simulation is required to predict the behavior of CO2 and its interaction with the oil and reservoir rock.", False),
 ("AI Approach Advances Predictive Precision in CO2 Minimum Miscibility Pressure", "/ai-approach-advances-predictive-precision-in-co-minimum-miscibility-pressure-restricted", "Enhanced recovery", "January 1, 2025", "",
  "The objective of this study is to develop an explainable data-driven method using five different methods to create a model using a multidimensional data set with more than 700 rows of data for predicting minimum miscibility pressure.", True),
 ("Machine Learning Enables Data-Driven Predictions of CO2 EOR Numerical Studies", "/machine-learning-enables-data-driven-predictions-of-co-eor-numerical-studies-restricted", "Enhanced recovery", "January 1, 2025", "",
  "The authors present an open-source framework for the development and evaluation of machine-learning-assisted data-driven models of CO2 enhanced oil recovery processes to predict oil production and CO2 retention.", True),
 ("Physics-Informed ML Improves Forecasting, Connectivity Identification for CO2 EOR", "/physics-informed-ml-improves-forecasting-connectivity-identification-for-co-eor-restricted", "Enhanced recovery", "January 1, 2025", "",
  "The authors of this paper propose hybrid models, combining machine learning and a physics-based approach, for rapid production forecasting and reservoir-connectivity characterization using routine injection or production and pressure data.", True),
 ("Measurement of Acrylamido Tertiary Butyl Sulfonate Polymer Retention on Limestone", "/measurement-of-acrylamido-tertiary-butyl-sulfonate-polymer-retention-on-limestone-by-three-methods-under-varying-temperature-and-oil-presence", "SPE News", "December 26, 2024", "SPE Journal",
  "This polymer retention study examines temperature effect on an ATBS-based polymer, using single- and two-phase retention studies and different analytical methods in the presence and absence of oil.", False),
 ("New Joint Venture Targets US Carbon Sequestration and Enhanced Oil Recovery Projects", "/new-joint-venture-targets-us-carbon-sequestration-and-enhanced-oil-recovery-projects", "Carbon capture and storage", "November 19, 2024", "HSE Now",
  "The partnership between GLJ and Energy Fuse Group aims to leverage the expertise of both companies in project management, operational design, and subsurface and commercial evaluations to facilitate effective CO2 storage solutions.", False),
 ("Technical Report Provides IOR and EOR Terminology Clarifications and Recommendations for the SPE Community", "/technical-report-provides-ior-and-eor-terminology-clarifications-and-recommendations-for-the-spe-community", "Enhanced recovery", "November 8, 2024", "",
  "The SPE IOR-EOR Terminology Review Committee has released its recommendations for the use of IOR, EOR, and newly introduced term, assisted oil recovery (AOR).", False),
 ("Locally Produced Sustainable and Resilient Surfactants for Enhanced Oil Recovery", "/locally-produced-sustainable-and-resilient-surfactants-for-enhanced-oil-recovery-restricted", "Enhanced recovery", "November 1, 2024", "",
  "This study explores the potential of locally produced surfactants for enhanced oil recovery in high-temperature and high-salinity reservoir environments.", True),
 ("Polymer-Injection Pilot in Colombian Field Indicates Reduced Carbon Footprint", "/polymer-injection-pilot-in-colombian-field-indicates-reduced-carbon-footprint-restricted", "Enhanced recovery", "November 1, 2024", "",
  "This paper describes a polymer-injection pilot in the Chichimene heavy oil field in Colombia.", True),
 ("Polymer Flooding Reduces Emissions and Energy Consumption in the North Sea", "/polymer-flooding-reduces-emissions-and-energy-consumption-in-the-north-sea-restricted", "Enhanced recovery", "November 1, 2024", "",
  "This paper describes a project in the heavy oil Captain field in the UK sector of the North Sea in which reduced environmental impact dovetails with improved economics.", True),
 ("EOR Operations (2024, Nov)", "/eor-operations-2024-v2", "Enhanced recovery", "November 1, 2024", "Elizabeth Barsotti",
  "International agreements and national policies on environmental sustainability are changing the outlook for enhanced oil recovery globally. These changes are highlighted by both monetary and intellectual commitments by oil companies around the world.", False),
 ("Study Investigates Hydrate Formation Risk in WAG Changeover Operations", "/study-investigates-hydrate-formation-risk-in-wag-changeover-operations-restricted", "Flow assurance", "November 1, 2024", "",
  "This study investigates hydrate formation in a water-alternating-gas injection well under water-to-gas and gas-to-water changeover operations.", True),
 ("Cyclic Gas Injection in Low-Permeability Oil Reservoirs: Progress in Modeling and Experiments", "/cyclic-gas-injection-in-low-permeability-oil-reservoirs-progress-in-modeling-and-experiments", "Enhanced recovery", "October 28, 2024", "SPE Journal",
  "This paper presents a comprehensive literature review and critical examination of the published modeling and experimental studies regarding the recovery mechanisms of cyclic gas injection and the conditions under which the process can enhance oil recovery with the aim to identify lessons learned and areas in need of further study.", False),
 ("'Supercharged' Shale EOR: A Liquid-Hydrocarbon-Based Approach Enters the Fray", "/supercharged-shale-eor-a-liquid-hydrocarbon-based-approach-enters-the-fray-restricted", "Enhanced recovery", "October 1, 2024", "Trent Jacobs",
  "Shale Ingenuity's first pilot used common natural gas liquids to boost daily output 30-fold from a low-producing horizontal well in Texas.", True),
 ("Multidisciplinary Approach Underpins Development of Marginal Presalt Reservoir", "/multidisciplinary-approach-underpins-development-of-marginal-presalt-reservoir-restricted", "Field/project development", "September 1, 2024", "",
  "This paper presents a multidisciplinary view of the evolution of a development project for the central area of Sururu and the method applied to address challenges and propose solutions.", True),
 ("Reliable Equivalent Alkane Carbon Number Determination for Dead and Live Crudes in Microemulsion Systems", "/reliable-equivalent-alkane-carbon-number-determination-for-dead-and-live-crudes-in-microemulsion-systems", "Enhanced recovery", "August 28, 2024", "SPE Journal",
  "This paper presents a clear and consistent method for determining dead and live crude EACNs using a single reliable method, highlighting a graphical way to determine the optimal salinity and its uncertainties using real data.", False),
 ("Investigating the Effect of Water Softening on Polymer Adsorption Onto Carbonates", "/investigating-the-effect-of-water-softening-on-polymer-adsorption-onto-carbonates-trough-single-phase-and-two-phase-experiments", "Enhanced recovery", "August 20, 2024", "SPE Journal",
  "This paper presents a unique investigation into determining the sufficient concentration of hardness ions required to significantly reduce the adsorption of acrylamide-tertiary-butyl-sulfonate-based polymer with a focus on mitigating polymer retention in carbonate formations using softened brine.", False),
 ("ONGC Seeks Technical Help To Boost Offshore Production", "/ongc-seeks-technical-help-to-boost-offshore-production", "Field/project development", "August 5, 2024", "Pat Davis Szymczak",
  "India's state oil company is accepting proposals from potential technical service partners until 15 September for EOR projects in the Arabian Sea.", False),
 ("IOR and EOR Terminology Clarifications and Recommendations for the SPE Community: Public Comments Period Open", "/ior-and-eor-terminology-clarifications-and-recommendations-for-the-spe-community-public-comments-period-open", "SPE News", "August 1, 2024", "",
  "The SPE IOR-EOR Terminology Review Committee has opened a period for public comments on a draft technical report.", False),
 ("Data-Driven Approach Enhances Liquid-Loading Detection and Prediction", "/data-driven-approach-enhances-liquid-loading-detection-and-prediction-restricted", "Enhanced recovery", "August 1, 2024", "",
  "This paper describes a data-driven approach for liquid-loading detection and prediction that harnesses high-frequency gas-rate and tubinghead-pressure measurements to identify the onset of liquid loading and correct critical rates computed by empirical methods.", True),
 ("Numerical Rate Transient Analysis Workflow Applied to Dry Gas Wells", "/numerical-rate-transient-analysis-workflow-applied-to-dry-gas-wells-restricted", "Enhanced recovery", "August 1, 2024", "",
  "This paper outlines the importance of numerical rate transient analysis for dry gas wells, describing a simple, fully penetrating planar fracture model.", True),
 ("Downhole Hydrogen-Generation System Stimulates Challenging Formations in Kuwait", "/downhole-hydrogen-generation-system-stimulates-challenging-formations-in-kuwait", "Unconventional/complex reservoirs", "July 1, 2024", "",
  "This paper highlights an approach of using active hydrogen to stimulate hard-to-recover formations from candidate-well selection through pilot execution and evaluation.", True),
 ("Extended Laterals and Hydraulic Fracturing Redevelop Tight Fractured Carbonates", "/extended-laterals-and-hydraulic-fracturing-redevelop-tight-fractured-carbonates", "Unconventional/complex reservoirs", "July 1, 2024", "",
  "The authors investigate the utility of applying unconventional technology to low- or variably producing carbonate reservoirs to increase estimated ultimate recovery and decrease development-scale variability.", False),
 ("2024 SPE Pioneers of Improved Oil Recovery", "/2024-spe-pioneers-of-improved-oil-recovery", "Enhanced recovery", "July 1, 2024", "Jennifer Pallanich",
  "The honor recognizes recipients for their lasting and significant contributions in the field of IOR.", False),
 ("Hilcorp Acquires Eni's Beaufort Sea Oil Fields on Alaska's North Slope", "/hilcorp-acquires-enis-beaufort-sea-oil-fields-on-alaskas-north-slope", "Asset/portfolio management", "June 29, 2024", "Pat Davis Szymczak",
  "By acquiring Eni's two producing shallow-water assets, Hilcorp will become the largest offshore oil producer on Alaska's North Slope.", False),
 ("Shale EOR Prospects Remain Dim This Decade, Yet Experts Call for Sustained Investment and Optimism", "/shale-eor-prospects-remain-dim-this-decade-yet-experts-call-for-sustained-investment-and-optimism", "Unconventional/complex reservoirs", "June 26, 2024", "Trent Jacobs",
  "Pilots and papers are plentiful, but the shale sector has no big enhanced oil recovery projects to speak of. It may just have to stay that way for a while.", False),
 ("A Data-Driven Approach To Optimize WAG Injection in a Large Carbonate Field", "/a-data-driven-approach-to-optimize-wag-injection-in-a-large-carbonate-field", "Enhanced recovery", "June 3, 2024", "Data Science and Digital Engineering",
  "This study proposes a hybrid model that combines the capacitance/resistance model, a machine-learning model, and an oil model to assess and optimize water-alternating-gas (WAG) injectors in a carbonate field.", False),
 ("Underbalanced Coiled Tubing Approach Targets Natural Fractures in Tight Sandstones", "/underbalanced-coiled-tubing-approach-targets-natural-fractures-in-tight-sandstones", "Enhanced recovery", "June 1, 2024", "",
  "This paper describes the application of an underbalanced coiled tubing technology in tight sandstones, using an integrative approach that incorporates petrophysical, geophysical, and reservoir engineering data.", True),
 ("Hydraulic Fracturing Optimizes Extraction of Reservoir Initially Considered Secondary", "/hydraulic-fracturing-optimizes-extraction-of-reservoir-initially-considered-secondary", "Enhanced recovery", "June 1, 2024", "",
  "This paper describes a hydraulic fracturing pilot project using a technique that generates higher fracture conductivity to reduce the drawdown during production and improve connection through laminations.", True),
 ("Fracture Stimulation Increases Production in Challenging North African Completions", "/fracture-stimulation-increases-production-in-challenging-north-african-completions", "Enhanced recovery", "June 1, 2024", "",
  "This paper presents a case study of a North African oil field producing from two Ordovician sands with differing permeabilities where significant benefit was achieved by fracture stimulating one or both intervals in two wells.", True),
 ("Limited-Entry-Liner Well Stimulated Effectively With a Viscoelastic Diverter-Acid System", "/limited-entry-liner-well-stimulated-effectively-with-a-viscoelastic-diverter-acid-system", "Acidizing/stimulation", "June 1, 2024", "",
  "This paper describes the stimulation of a horizontal water-injection well with a limited-entry-liner completion in an onshore carbonate reservoir using a large volume of viscoelastic diverter-acid fluid system ahead of the main acid stage.", True),
 ("Nanoparticle-Based Fluids Reverse Long-Term Hydrocarbon Decline", "/nanoparticle-based-fluids-reverse-long-term-hydrocarbon-decline", "Acidizing/stimulation", "June 1, 2024", "",
  "This paper details a successful pilot to improve long-term well performance using acid stimulation aided by a tailored metal oxide nanoparticle-based fluid in the Wolfcamp A formation.", True),
 ("Polymer-Assisted WAG Injection Improves CO2 Flow Properties in Porous Media", "/polymer-assisted-wag-injection-improves-co2-flow-properties-in-porous-media", "Enhanced recovery", "June 1, 2024", "",
  "In this paper, the authors propose polymer-assisted water-alternating-gas (WAG) injection as an alternative method to reduce gas mobility while reducing the mobility of the aqueous phase and, consequently, improving WAG performance.", True),
 ("Study Explores Effect of Solids on Topside Operations in an EOR Context", "/study-explores-effect-of-solids-on-topside-operations-in-an-eor-context-v1", "Enhanced recovery", "June 1, 2024", "",
  "The authors of this paper study the effect of solids particles on oil/water separators and on produced-water treatment.", True),
 ("Sensitivity Analysis of CO2 Minimum Miscibility Pressure Optimizes Gas-Injection EOR", "/sensitivity-analysis-of-co2-minimum-miscibility-pressure-optimizes-gas-injection-eor", "Enhanced recovery", "June 1, 2024", "",
  "The authors present an efficient microfluidic platform to measure high-quality minimum miscibility pressure data of CO2 with various impurities faster and easier.", True),
 ("Model Captures Carbonate Matrix Acidizing in Horizontal Well Completions", "/model-captures-carbonate-matrix-acidizing-in-horizontal-well-completions", "Acidizing/stimulation", "June 1, 2024", "",
  "This study introduces a detailed model to capture the physics and chemistry of acid flow in complex horizontal wells completed in carbonate formations.", True),
 ("Far-Field Diverters Protect Parent-Well Production in Unconventional Wells", "/far-field-diverters-protect-parent-well-production-in-unconventional-wells", "Enhanced recovery", "June 1, 2024", "",
  "The authors of this paper describe a project in which far-field diverters were pumped to mitigate wellbore sanding and production loss in existing parent wells.", True),
 ("EOR Operations (2024)", "/eor-operations-2024", "Enhanced recovery", "June 1, 2024", "Kristian Mogensen",
  "The EOR scene has evolved as well. Low-salinity waterflooding, originally thought to apply only in certain sandstone reservoirs, appears to be able to unlock additional reserves also for some carbonate formations, although the fundamental mechanisms are different.", False),
 ("Acidizing (2024)", "/acidizing-2024", "Enhanced recovery", "June 1, 2024", "Imran Abbasy",
  "Engineers desperately need an alternative to acid placement through pipe, coiled tubing, or bullheading. For example, propellants have been around for years; however, their performance has not quite met the hype. Nevertheless, several case histories have been authored to suggest their efficacy.", False),
 ("Project Pursues Autonomous Waterflooding Operations Driven by AI", "/project-pursues-autonomous-waterflooding-operations-driven-by-ai", "Digital Oil Field", "May 1, 2024", "",
  "This paper presents the design and development of a prototype intelligent water-injection and smart allocation tool aimed at achieving autonomous waterflood operations.", True),
 ("Case Study: High-Energy Elastic-Wave-Based EOR Crosses Flow Barriers in a Canyon Sand To Reverse Oil Decline", "/case-study-high-energy-elastic-wave-based-eor-crosses-flow-barriers-in-a-canyon-sand-to-reverse-oil-decline", "Enhanced recovery", "May 1, 2024", "Bill Wooden",
  "In southwest Texas, a producer faced imminent shutdown of its canyon sand field due to rapid production decline. Field tests using elastic-wave EOR determined whether the field could be revitalized or if a costly shut-in process was inevitable.", True),
 ("The Impact of Autonomous Inflow Control Valve on Improved Recovery in a Thin-Oil-Rim Reservoir", "/the-impact-of-autonomous-inflow-control-valve-on-improved-recovery-in-a-thin-oil-rim-reservoir", "Reservoir", "April 9, 2024", "SPE Journal",
  "Oil production from thin-oil-rim fields can be a challenge considering early gas breakthrough and high gas/oil ratio. This study evaluates the performance of autonomous inflow control valves and their effectiveness in improved oil recovery in such fields.", False),
 ("SAGD Trial in Omani Heavy Oil Field Overcomes Suboptimal Conditions", "/sagd-trial-in-omani-heavy-oil-field-overcomes-suboptimal-conditions", "Unconventional/complex reservoirs", "April 1, 2024", "",
  "This paper describes the potential, challenges, and opportunities of using a modified steam-assisted gravity drainage configuration in the Mukhaizna heavy oil field in suboptimal operating conditions.", True),
 ("Chemical Additives Assist Oil-in-Water Emulsion Formation in SAGD", "/chemical-additives-assist-oil-in-water-emulsion-formation-in-sagd", "Unconventional/complex reservoirs", "April 1, 2024", "",
  "This study aims at understanding the effect of a surfactant known as a high-temperature emulsifying agent as an additive to the steam-assisted gravity drainage process and the possibility of forming oil-in-water emulsions.", True),
 ("Hybrid Technology Incorporated Into Colombian Heavy Oil Field Development Plan", "/hybrid-technology-incorporated-into-colombian-heavy-oil-field-development-plan", "Unconventional/complex reservoirs", "April 1, 2024", "",
  "This paper describes the implementation of a hybrid technology of cyclic steam stimulation and foam into the heavy oil field development plans of the Middle Magdalena Valley basin in Colombia.", True),
 ("Case Study: Innovative Sand-Screen Technology Resolves Offshore Nigeria Water-Injection Issues", "/case-study-innovative-sand-screen-technology-resolves-offshore-nigeria-water-injection-issues", "Enhanced recovery", "April 1, 2024", "Mojtaba Moradi",
  "To avoid costly interventions like sidetracking or wellbore abandonment, a check-valve system was installed near the sandface within three injector wells which prevented the mobilization of fines from the reservoir into the wellbore by stopping backflow.", True),
 ("Guest Editorial: The Difference Between CO2 EOR and CCS Injection Well Metallurgy", "/guest-editorial-the-difference-between-co2-eor-and-ccs-injection-well-metallurgy", "Carbon capture and storage", "March 1, 2024", "Bruce Craig",
  "The long, successful history of various metallurgies in EOR wells has been cited as sufficient to allow the same completions for CCS injection wells. The lack of actual data on the long-term performance of these alloys in EOR wells in combination with the more-stringent requirements for Class VI wells suggests otherwise.", False),
 ("Reservoir Modeling Predicts Effect of Cold-Water Injection on Geothermal PTA", "/reservoir-modeling-predicts-effect-of-cold-water-injection-on-geothermal-pta", "Enhanced recovery", "February 1, 2024", "",
  "In this paper, the effect of cold-water injection on pressure transient analysis (PTA) of geothermal reservoirs is studied by varying the temperature of the injected cold water from room temperature to reservoir temperature.", True),
 ("EOR Modeling (2024)", "/eor-modeling-2024", "Enhanced recovery", "January 1, 2024", "Hussein Hoteit",
  "These papers underscore the industry's shift toward more efficient practices, each contributing a crucial piece to the larger puzzle of EOR.", False),
 ("Model Shows Computational Gains, Preserves Accuracy in Tight Rock EOR", "/model-shows-computational-gains-preserves-accuracy-in-tight-rock-eor", "Enhanced recovery", "January 1, 2024", "",
  "The authors of this paper present an advanced dual-porosity, dual-permeability (A-DPDK) work flow that leverages benefits of discrete fracture and DPDK modeling approaches.", True),
 ("Machine-Learning-Based Solution Predicts Fluid Properties for Gas-Injection Data", "/machine-learning-based-solution-predicts-fluid-properties-for-gas-injection-data", "Enhanced recovery", "January 1, 2024", "",
  "The authors of this paper present a machine-learning-based solution that predicts pertinent gas-injection studies from known fluid properties such as fluid composition and black-oil properties.", True),
 ("Work Flow Screens Surfactants for EOR Through Wettability Alteration", "/work-flow-screens-surfactants-for-eor-through-wettability-alteration", "Enhanced recovery", "January 1, 2024", "",
  "This study presents a novel approach to screen thermally stable surfactants at high pressures and high temperatures for the explicit purpose of wettability alteration in the operator's Eagle Ford acreage.", True),
 ("Process Synthesizes Janus Carbon Nanofluids From Waste Plastics for EOR", "/process-synthesizes-janus-carbon-nanofluids-from-waste-plastics-for-eor", "Enhanced recovery", "November 1, 2023", "",
  "This paper presents a novel sustainable cost-effective method developed to scale up synthesis of Janus carbon nanoparticles from waste plastic feedstock by combined pyrolysis, chemical functionalization, and pulverization.", True),
 ("Study Reviews Largest ASP Project From Laboratory to Pilots and Field Application", "/study-reviews-largest-asp-project-from-laboratory-to-pilots-and-field-application", "Enhanced recovery", "November 1, 2023", "",
  "This paper presents a systematic review of the largest alkaline-surfactant-polymer flood project in the world, applied to the largest oil field in China.", True),
 ("Study Evaluates CO2 Storage Potential During CO2 Mobility-Control Optimization", "/study-evaluates-co2-storage-potential-during-co2-mobility-control-optimization", "Enhanced recovery", "November 1, 2023", "",
  "In this paper, the authors evaluate the simultaneous optimization of CO2 storage and oil recovery using multiple injection strategies.", True),
]

# ----------------------------------------------------------------------------
# Wells-Engineering discipline classification (keyword rules)
# ----------------------------------------------------------------------------
DISCIPLINE_RULES = [
    ("Field Development", [
        "field development","development plan","development project","field-project","field/project",
        "epci","trunkline","project management","project-management","appraisal","marginal field",
        "presalt","well-network-design","well network","tieback","infrastructure","fdp","redevelop",
        "rehab","acquire","acquisition","joint venture","exploration and development"]),
    ("Drilling & Well Construction", [
        "drilling","drill","casing","cementing","zonal isolation","directional","horizontal well",
        "extended lateral","laterals","wellbore","sidetrack","liner","completion well metallurgy",
        "metallurgy","class vi well","well construction","drilling-location","openhole"]),
    ("Completions & Stimulation", [
        "completion","fracturing","frac","hydraulic fractur","stimulat","acidizing","acid","proppant",
        "perforat","sand screen","sand-screen","sand control","diverter","fishbone","limited-entry",
        "matrix acid","skin","intelligent completion","closed-loop","fracture conductivity","stimulation",
        "well integrity"]),
    ("Production & Well Performance", [
        "artificial lift","gas-lift","gas lift","esp","electrical submersible","inflow control","icd","aicv",
        "aocd","flow-control device","flow control","liquid loading","gas/oil ratio","gor","rate transient",
        "well performance","well control","intervention","surveillance","huff","cyclic steam","steam injection",
        "thin-oil-rim","oil-rim","oil rim","decline","drawdown","gas separation","self-flow","subsurface safety"]),
    ("Facilities & Flow Assurance", [
        "facilit","topside","separator","separation","produced-water","produced water","flow assurance",
        "hydrate","pipeline","subsea","processing","surface facilit","gas facilities","permeate","sales gas",
        "injectivity","water-injection","water injection","check-valve"]),
    ("Reservoir & EOR", [
        "enhanced oil recovery","enhanced recovery","eor","waterflood","polymer","surfactant","wag",
        "water-alternating-gas","co2","minimum miscibility","miscibility","sagd","steam-assisted","gravity drainage",
        "wettability","displacement efficiency","recovery mechanism","gas injection","gas-injection","injectant",
        "in-situ combustion","asp","alkaline","biosurfactant","ferrofluid","nanofluid","nanoparticle","microemulsion",
        "low-salinity","reservoir simulation","reservoir-fluid","connectivity","permeability","relative permeability",
        "phase behavior","equation of state","condensate","elastic-wave","wormhole"]),
    ("CCUS & Decarbonization", [
        "carbon sequestration","carbon-dioxide storage","co2 storage","co2-sequestration","sequestration",
        "ccs","ccus","carbon capture","carbon storage","carbon footprint","emission","greenhouse-gas",
        "decarboniz","saline aquifer","carbon-dioxide content"]),
    ("Digital, AI & Modeling", [
        "machine learning","machine-learning","deep-learning","deep learning","artificial intelligence",
        "artificial-intelligence","data-driven","data driven","ai ","physics-informed","physics-inspired",
        "agentic","predictive model","proxy-model","proxy model","forecasting","capacitance/resistance",
        "autonomous","numerical simulation","modeling tool","explainable","fiber-optic","real-time"]),
]

WELLS_CORE = {"Field Development","Drilling & Well Construction","Completions & Stimulation",
              "Production & Well Performance","Facilities & Flow Assurance"}

# region / play / operator dictionaries for context extraction
PLAYS = ["Permian","Bakken","Eagle Ford","Midland","Delaware Basin","Wolfcamp","Niobrara","Montney",
         "Haynesville","Marcellus","Scoop","Stack","North Slope","Pikka","Permian shale","Austin Chalk",
         "Maverick Basin","Captain field","Chichimene","Mukhaizna","Sururu","Kirkuk","Apani","Project Cape",
         "Middle Magdalena","canyon sand","Daqing","Surmont","Beaufort Sea"]
REGIONS = ["North Sea","Permian Basin","Alaska","Saudi Arabia","Middle East","Colombia","North Africa",
           "Nigeria","Kuwait","Oman","Omani","Malaysia","China","Iraq","Texas","Arabian Sea","Utah","UK","Canada","Colombian"]
OPERATORS = ["Chevron","Occidental","Aramco","Saipem","BP","Hilcorp","Eni","ONGC","Shale Ingenuity","GLJ",
             "Energy Fuse","Halliburton","NETL"]
METHODS = [
    ("CO2 injection / miscible gas flooding", ["co2","carbon dioxide","carbon-dioxide","miscib","minimum miscibility"]),
    ("Water-alternating-gas (WAG)", ["wag","water-alternating-gas","water alternating gas"]),
    ("Polymer flooding", ["polymer","polyacrylamide","atbs","viscosit"]),
    ("Surfactant / chemical EOR", ["surfactant","asp","alkaline","wettability","microemulsion","biosurfactant","ketone"]),
    ("Hydraulic fracturing", ["hydraulic fractur","fracturing","frac ","closed-loop","far-field diverter","proppant"]),
    ("Acidizing / matrix stimulation", ["acidizing","acid ","matrix acid","fishbone","diverter-acid","wormhole"]),
    ("SAGD / thermal recovery", ["sagd","steam-assisted","gravity drainage","cyclic steam","steam injection","in-situ combustion","thermal"]),
    ("Inflow / flow control (ICD/AICV/AICD)", ["inflow control","icd","aicv","aocd","flow-control device","flow control device"]),
    ("Artificial lift (ESP / gas lift)", ["esp","electrical submersible","gas-lift","gas lift","artificial lift"]),
    ("Coiled tubing", ["coiled tubing","coiled-tubing"]),
    ("Sand control", ["sand screen","sand-screen","sand control","fines"]),
    ("Nanotechnology / nanofluids", ["nanoparticle","nanofluid","janus"]),
    ("Machine learning / AI", ["machine learning","machine-learning","deep-learning","deep learning","artificial intelligence","artificial-intelligence","data-driven","physics-informed","physics-inspired","agentic"]),
    ("Reservoir simulation / modeling", ["simulation","modeling","model ","equation of state","dual-porosity","compositional","proxy"]),
    ("Geothermal", ["geothermal"]),
    ("Carbon storage / CCUS", ["sequestration","ccs","ccus","carbon capture","co2 storage","carbon storage"]),
    ("Liquid loading / well deliquification", ["liquid loading","liquid-loading","critical gas rate"]),
]

def classify(text):
    t = text.lower()
    hits = []
    for disc, kws in DISCIPLINE_RULES:
        if any(k in t for k in kws):
            hits.append(disc)
    if not hits:
        hits = ["Reservoir & EOR"]
    return hits

def find_terms(text, vocab):
    out = []
    for term in vocab:
        if term.lower() in text.lower():
            out.append(term)
    # de-dup, keep order
    seen=set(); res=[]
    for x in out:
        if x.lower() not in seen:
            seen.add(x.lower()); res.append(x)
    return res

def find_methods(text):
    out=[]
    for label,kws in METHODS:
        if any(k in text.lower() for k in kws):
            out.append(label)
    return out

CHALLENGE_KWS = ["challeng","difficult","issue","problem","loss","degrad","risk","suboptimal","decline",
                 "breakthrough","barrier","heterogen","hard-to-recover","little-understood","do not always align",
                 "costly","corros","fines","sanding","self-flow","high-temperature","high-salinity","tectonic",
                 "complex","uncertaint"]

def sentences(text):
    # naive splitter
    parts = re.split(r'(?<=[.;])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]

VALUE_KWS = {
    "recovery":"increased / improved hydrocarbon recovery",
    "oil production":"higher oil production",
    "production":"sustained or increased production",
    "injectivity":"preserved injectivity",
    "injectant cost":"reduced injectant cost",
    "cost":"cost / economic efficiency",
    "emission":"lower emissions",
    "carbon footprint":"reduced carbon footprint",
    "storage":"secure CO2 storage",
    "sequestration":"CO2 sequestration value",
    "estimated ultimate recovery":"higher estimated ultimate recovery (EUR)",
    "economics":"improved project economics",
    "project value":"increased project value",
    "sales gas":"monetized sales gas",
    "barrels":"unlocking additional barrels",
}

def build_summary(rec):
    abstract = rec["abstract"]
    title = rec["title"]
    discs = rec["disciplines"]
    plays = find_terms(abstract+" "+title, PLAYS)
    regions = find_terms(abstract+" "+title, REGIONS)
    operators = find_terms(abstract+" "+title, OPERATORS)
    methods = find_methods(abstract+" "+title)
    sents = sentences(abstract)

    # CONTEXT
    geo = []
    if plays: geo.append("play/field: " + ", ".join(plays[:3]))
    if regions: geo.append("region: " + ", ".join(regions[:3]))
    if operators: geo.append("operators/parties: " + ", ".join(operators[:3]))
    ctx = "Wells-engineering lens: " + " | ".join(discs) + "."
    if geo:
        ctx += " Setting from the brief - " + "; ".join(geo) + "."
    else:
        ctx += " The brief does not name a specific field or operator."

    # TECHNICAL
    tech = ""
    if methods:
        tech = "Methods/technologies referenced: " + ", ".join(methods) + ". "
    tech += "As stated in the brief: \"" + sents[0] + "\"" if sents else ""

    # BUSINESS PROBLEM & VALUE
    vals = []
    low = abstract.lower()
    for kw,label in VALUE_KWS.items():
        if kw in low and label not in vals:
            vals.append(label)
    if vals:
        biz = "Value levers indicated by the brief: " + "; ".join(sorted(set(vals))) + "."
    else:
        biz = "The brief frames the work within enhanced/improved oil recovery; specific economic figures are not stated publicly."

    # CHALLENGES
    chal_sents = [s for s in sents if any(k in s.lower() for k in CHALLENGE_KWS)]
    if chal_sents:
        challenges = " ".join(chal_sents)
    else:
        challenges = "The public brief does not enumerate specific operational challenges; it positions the work as a methodology/case advance within " + discs[0].lower() + "."

    # GAPS
    gaps = ("This is an abstract-faithful summary of a paywalled SPE paper. Quantitative results, "
            "full methodology, field data, and uncertainty/economics are in the source paper and are "
            "not reproduced in the public brief.")
    if not rec["locked"]:
        gaps = ("Summary built from the public brief only. Detailed methodology, datasets, and "
                "quantitative outcomes reside in the linked article/paper.")

    # WELLS-ENGINEERING RELEVANCE
    core = [d for d in discs if d in WELLS_CORE]
    if core:
        relevance = "High"
        rel_note = ("Directly touches integrated wells-engineering scope ("
                    + ", ".join(core) + ").")
    elif any(d in ("Reservoir & EOR","Production & Well Performance") for d in discs):
        relevance = "Medium"
        rel_note = "Subsurface/recovery focus that informs well and completion design decisions."
    else:
        relevance = "Context"
        rel_note = "Adjacent topic (modeling, CCUS, or industry news) providing strategic context."

    return {
        "context": ctx,
        "technical": tech,
        "business": biz,
        "challenges": challenges,
        "gaps": gaps,
        "summary": abstract,
        "relevance": relevance,
        "relevance_note": rel_note,
        "plays": plays, "regions": regions, "operators": operators, "methods": methods,
    }

# ----------------------------------------------------------------------------
# Assemble
# ----------------------------------------------------------------------------
records = []
seen=set()
for (title, slug, tag, date, author, abstract, locked) in R:
    url = BASE + slug
    if url in seen:
        continue
    seen.add(url)
    dt = datetime.strptime(date, "%B %d, %Y")
    disciplines = classify(title + " " + abstract + " " + tag)
    rec = {
        "title": title, "url": url, "source_tag": tag, "author": author or "JPT / SPE",
        "date": date, "iso": dt.strftime("%Y-%m-%d"), "year": dt.year,
        "ym": dt.strftime("%Y-%m"), "ts": int(dt.timestamp()),
        "locked": locked, "abstract": abstract, "disciplines": disciplines,
    }
    rec.update(build_summary(rec))
    records.append(rec)

records.sort(key=lambda r: r["ts"], reverse=True)

# stats
from collections import Counter
disc_counter = Counter()
for r in records:
    for d in r["disciplines"]:
        disc_counter[d]+=1
method_counter = Counter()
for r in records:
    for m in r["methods"]:
        method_counter[m]+=1
year_counter = Counter(r["year"] for r in records)
rel_counter = Counter(r["relevance"] for r in records)

meta = {
    "source": "https://jpt.spe.org/topic/enhanced-recovery",
    "generated": datetime.now().strftime("%Y-%m-%d"),
    "count": len(records),
    "date_min": min(r["iso"] for r in records),
    "date_max": max(r["iso"] for r in records),
    "disciplines": disc_counter.most_common(),
    "methods": method_counter.most_common(),
    "years": sorted(year_counter.items()),
    "relevance": rel_counter.most_common(),
}

rules = {
    "disciplines": DISCIPLINE_RULES,
    "plays": PLAYS,
    "regions": REGIONS,
    "operators": OPERATORS,
    "methods": METHODS,
    "value_kws": VALUE_KWS,
    "challenge_kws": CHALLENGE_KWS,
    "wells_core": sorted(WELLS_CORE),
}

out = {"meta": meta, "records": records, "rules": rules}
with open("data.json","w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

print("records:", len(records))
print("date range:", meta["date_min"], "->", meta["date_max"])
print("disciplines:", disc_counter.most_common())
print("relevance:", rel_counter.most_common())
print("top methods:", method_counter.most_common(8))
