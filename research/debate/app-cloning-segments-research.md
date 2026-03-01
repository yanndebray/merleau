# App Cloning via Video Understanding: Target Segments, Concrete Examples, and Persona Analysis

## Deep Research Report for Merleau SaaS Offering

---

## Table of Contents

1. [Legacy UI Cloning Opportunities](#1-legacy-ui-cloning-opportunities)
2. [Vertical Niche Segments](#2-vertical-niche-segments)
3. [Concrete App Examples for Video-Based Cloning](#3-concrete-app-examples-for-video-based-cloning)
4. [Persona Deep Dive: Coder vs Non-Coder](#4-persona-deep-dive-coder-vs-non-coder)
5. [The App Cloning Workflow](#5-the-app-cloning-workflow)
6. [Strategic Recommendations](#6-strategic-recommendations)

---

## 1. Legacy UI Cloning Opportunities

### Market Context

The application modernization services market is projected to grow from USD 20.55 billion in 2025 to USD 81.24 billion by 2034, exhibiting a CAGR of 16.5%. Approximately 78% of enterprises worldwide are currently engaged in some level of modernization activity. The legacy software modernization service market specifically was valued at $38.4 billion in 2024 and is expected to reach $80 billion by 2035. This is an enormous, structurally growing market -- and a large portion of it involves replacing or reskinning outdated user interfaces.

### 1.1 Enterprise ERP Systems (SAP, Oracle Forms)

**SAP GUI Transactions:**
SAP's GUI has remained largely untouched for 28 years. Users frequently complain that screens like "create sales order" (transaction VA01) are far too complex, with users needing only 10% of the available fields. SAP has attempted to modernize with SAP Fiori (introduced with S/4HANA in 2015), but migration is slow and incomplete -- thousands of transaction screens remain in the old GUI format across millions of installations.

- **Why video cloning adds value:** SAP workflows are deeply sequential and stateful. A user creating a purchase order navigates through multiple transaction codes (T-codes), enters data across tabbed screens, triggers validations, and receives confirmation screens. A screencast captures the *exact sequence*, the *timing between steps*, the *conditional branches* (what happens when a field validation fails), and the *data dependencies* between screens. Static screenshots would require dozens of annotated images and still miss the flow logic.

**Oracle Forms (6i and later):**
Organizations have invested years and millions of dollars attempting to migrate from Oracle Forms, with some projects completing only 15% after three years of effort. The shrinking talent pool of Oracle Forms developers makes maintenance increasingly expensive. Versions 6i and below are particularly challenging to upgrade.

- **Why video cloning adds value:** Oracle Forms applications have complex master-detail relationships, LOV (List of Values) popups, and trigger-based field validations that are impossible to understand from a single screenshot. A screencast reveals the cascade of events: selecting a value in one field populates three others, tab order matters, and modal dialogs appear conditionally.

### 1.2 AS/400 Green Screen Terminal Applications

The AS/400 (IBM i), launched in 1988, remains the backbone of industries ranging from banking and logistics to healthcare and retail. Green screen terminals are still widely used because they are tightly integrated with core business processes, highly reliable, and offer low total cost of ownership. However, fewer developers today are familiar with the IBM i platform, and experienced COBOL/RPG developers are retiring.

Common modernization approaches include "screen scraping" (converting green-screen interfaces into graphical web-based UIs without changing the underlying code) and "refacing" tools that apply a modern GUI over existing 5250 screens.

- **Why video cloning adds value:** Green screen applications have a distinctive interaction model -- function key navigation (F3=Exit, F5=Refresh, F12=Cancel), command-line inputs, and menu-driven hierarchies. A screencast captures the exact keystrokes, the screen transitions, and the data entry patterns that define the workflow. This is information that is literally invisible in a screenshot.

### 1.3 Lotus Notes / HCL Domino Applications

Thousands of enterprises continue to rely on custom-built Lotus Notes applications for internal operations, workflows, and collaboration. Versions 9 and 10 are now officially out of support, creating urgent migration pressure. Hundreds of companies have used platforms like OutSystems to replace critical Notes applications, including Japanese infrastructure giant Maeda Corporation, which migrated thousands of Notes databases to modern cloud-based applications.

- **Why video cloning adds value:** Lotus Notes applications are notoriously idiosyncratic -- each organization customized them heavily. There is no "standard" Notes app to reference. The only way to understand what a specific Notes workflow does is to watch someone use it. Video captures the navigation between views, the form layouts, the approval routing, and the document lifecycle that define each custom application.

### 1.4 Government and Public Sector Legacy Systems

Eight of the 11 most critical federal legacy systems identified by the U.S. GAO use outdated languages. Both of the Department of the Treasury's selected systems run on COBOL and Assembly Language Code. A Dell study revealed that more than 70% of federal IT decision-makers in the USA, Germany, the UK, Japan, Brazil, India, and China use outdated software, with half saying their legacy software has exceeded its end-of-life date.

Examples include:
- Tax processing systems
- Social security and benefits management
- Unemployment claims systems
- Public records and permitting systems

- **Why video cloning adds value:** Government systems often have no documentation, no source code access, and no original developers available. The *only* way to understand what the system does may be to record someone using it. Video becomes the specification.

### 1.5 Healthcare / EHR Legacy Interfaces

Legacy EHR platforms have clunky interfaces, poor interoperability, and limited reporting. The American Medical Association reports that over 50% of physician burnout is tied to administrative burden, often exacerbated by poorly designed EHR interfaces. Legacy EHRs often lack modern encryption, access controls, and patching mechanisms.

- **Why video cloning adds value:** Healthcare workflows are safety-critical and deeply sequential -- a nurse entering medication orders follows a precise multi-step flow with verification screens, allergy checks, and dosage calculations. Video captures the clinical workflow end-to-end, including error states and confirmation dialogs that must be replicated exactly in any replacement system.

### 1.6 WinForms / Legacy .NET Desktop Applications

WinForms remains supported in .NET 8 but is Windows-only and in maintenance mode -- Microsoft has positioned .NET MAUI as its official cross-platform framework. Few developers want to work on legacy desktop tech, and experienced WinForms developers are becoming harder to find. Organizations are migrating to Blazor (web-based) or MAUI (cross-platform).

- **Why video cloning adds value:** Desktop applications have rich interaction patterns -- drag-and-drop, right-click context menus, keyboard shortcuts, dockable panels, tree view navigation -- that are difficult to document in text but trivially captured in video. A 3-minute screencast of a WinForms data entry application communicates more about its behavior than a 10-page specification document.

### What Makes These Good Candidates for Video-Based Cloning?

| Factor | Why Video Helps |
|--------|----------------|
| **No documentation** | Legacy apps often outlive their documentation. Video becomes the living spec. |
| **Complex multi-step workflows** | Sequential processes with branching logic are naturally captured by video's temporal dimension. |
| **State-dependent UI** | Screens that change based on prior inputs or user roles are invisible in screenshots. |
| **Institutional knowledge** | The person who knows how the system works is often about to retire. Video preserves their knowledge. |
| **Validation and error handling** | Error states, required field highlighting, and validation messages appear dynamically during use. |
| **No source code access** | Many legacy systems run on proprietary platforms where source code is unavailable or unintelligible. |

---

## 2. Vertical Niche Segments

### 2.1 Insurance

Insurers allocate roughly 70% of their IT budgets solely to maintaining outdated systems, which constrains innovation investments. Insurance firms launching new products encounter significant delays, with the average development cycle extending 6-9 months at costs of $400,000-$900,000 per product. Policy administration systems operate in silos, making modern integration difficult.

**Cloning targets:**
- Claims processing dashboards
- Policy administration screens
- Agent quoting tools
- Underwriting workflow interfaces

**Video value-add:** Insurance workflows involve complex conditional logic (coverage types, endorsements, riders) that manifest as dynamic form behavior -- fields appearing/disappearing, validation rules changing based on prior selections. Video captures this conditional UI behavior naturally.

### 2.2 Real Estate / Property Management

Legacy MLS systems store data in inconsistent formats across multiple databases. Most legacy systems from the early 2000s cannot handle modern AI algorithms, and performance degrades with complex calculations. Modern features (AI valuations, VR tours, predictive analytics) require full modernization.

**Cloning targets:**
- MLS listing entry interfaces
- Property management dashboards
- Tenant portal applications
- Rent roll and accounting screens
- Showing scheduling tools

**Video value-add:** Real estate software involves heavy map interactions, photo gallery management, and complex filtering/search that are best understood through use demonstration.

### 2.3 Logistics and Transportation

Legacy TMS platforms struggle with integrations, automation, and real-time data demands. Many require significant customization or development resources for even basic integrations, with systems charging extra for API access. One case study involved a logistics powerhouse overhauling 50+ applications from legacy code to modern UX.

**Cloning targets:**
- Dispatch boards and route planners
- Warehouse management screens
- Bill of lading entry forms
- Freight quoting and booking interfaces
- Driver management portals

**Video value-add:** Logistics interfaces are highly interactive -- dispatchers drag shipments onto routes, update statuses in real time, and monitor live dashboards. The temporal dimension of video captures the real-time update patterns and the speed at which operators need to interact.

### 2.4 Internal Tools and Admin Dashboards

Engineering teams spend 40% of their time building and maintaining internal tools, representing two full days every week that could be spent on product development. The internal tools market is served by platforms like Retool, Budibase, and Appsmith, but many companies still have bespoke admin panels built years ago.

**Cloning targets:**
- Customer support admin panels
- Content management dashboards
- User management interfaces
- Analytics and reporting dashboards
- Order management back-office tools

**Video value-add:** Internal tools are often completely undocumented and known only to specific team members. Recording a power user's workflow is the fastest path to understanding what the tool does and how it should be rebuilt.

### 2.5 Regional/Localized Software

Many legacy programs do not support Unicode, creating barriers for East Asian languages. Localization projects for Chinese and Japanese software require more engineering and testing work. In many regions, industry-specific software exists with no modern equivalent because the market is too small for major vendors.

**Cloning targets:**
- Japanese keiretsu management systems
- German Handwerk (trades) management software
- Brazilian nota fiscal (invoice) systems
- Regional accounting systems with local tax compliance
- Country-specific HR/payroll systems

**Video value-add:** Regional software often has no English documentation and may use domain-specific terminology that makes text-based specification challenging. Video with screen content in the original language can be analyzed by multilingual AI models (Gemini supports 100+ languages), extracting UI structure regardless of language.

### 2.6 Niche SaaS Tools Users Want Customized

**Cloning targets:**
- Vertical CRMs (real estate, recruiting, automotive dealerships)
- Industry-specific scheduling tools
- Niche project management variations
- Specialized billing/invoicing for specific industries
- Practice management software (legal, dental, veterinary)

**Video value-add:** Users often want "exactly like Tool X, but with these three changes." Recording their current workflow in Tool X, narrating what they wish was different, creates a specification that combines the existing design with the desired modifications -- something impossible with screenshots alone.

---

## 3. Concrete App Examples for Video-Based Cloning

### Tier 1: Simple (Landing Pages, Forms, Single-Screen Apps)

#### Example 1: Insurance Quote Form
**What it is:** A multi-step insurance quoting form with conditional fields (vehicle type changes available coverage options).
**Why video adds value over text:** The conditional field logic -- selecting "commercial vehicle" reveals fleet size fields, changes liability options, adds cargo coverage -- is a dynamic behavior sequence. Screenshots show one state; video shows the branching.
**Complexity:** Low-Medium

#### Example 2: SaaS Pricing Page with Interactive Calculator
**What it is:** A pricing page where sliders adjust user count, features toggle on/off, and the total updates in real time.
**Why video adds value:** The real-time calculation behavior, the slider interactions, and the visual feedback (highlighted tier changes, animated price updates) are temporal phenomena that screenshots flatten into a single moment.
**Complexity:** Low

#### Example 3: Patient Check-In Kiosk Interface
**What it is:** A touchscreen check-in flow at a medical clinic -- patient selects appointment, verifies insurance, signs consent forms.
**Why video adds value:** The step-by-step flow with branching (returning patient vs new patient), form validation, and signature capture is a sequential workflow best captured in motion.
**Complexity:** Low-Medium

### Tier 2: Medium (Multi-Screen Workflows, CRUD Applications)

#### Example 4: SAP Purchase Order Creation (Transaction ME21N)
**What it is:** A multi-tab enterprise form for creating purchase orders -- vendor selection, line items, delivery schedule, conditions.
**Why video adds value:** The workflow spans 6+ screens/tabs with data dependencies (selecting a vendor populates payment terms, selecting a material populates pricing). A screencast of an experienced user creating a real PO captures the *actual* workflow, not the theoretical one documented in training materials.
**Complexity:** Medium-High

#### Example 5: Legacy CRM Contact Management
**What it is:** An older Salesforce Classic or ACT! CRM with custom fields, activity tracking, opportunity pipeline, and reporting.
**Why video adds value:** CRM workflows involve navigation between related records (contact -> company -> opportunity -> activity), inline editing, and drag-and-drop pipeline management. Video captures the navigation patterns and the relationships between entities that make CRM usable.
**Complexity:** Medium

#### Example 6: Property Management Tenant Portal
**What it is:** A portal where tenants submit maintenance requests, view lease documents, make payments, and communicate with management.
**Why video adds value:** The complete tenant journey -- from login, through request submission (including photo upload and category selection), to tracking status updates -- is a multi-step workflow with status transitions best captured in video.
**Complexity:** Medium

#### Example 7: Oracle Forms Inventory Management
**What it is:** A legacy Oracle Forms application for warehouse inventory -- receiving, putaway, picking, and shipping workflows.
**Why video adds value:** Oracle Forms' master-detail relationships, LOV popups, and trigger-based validations create complex interaction chains. A screencast of a warehouse clerk processing a receipt captures the exact sequence of popups, auto-populated fields, and confirmation dialogs.
**Complexity:** Medium-High

### Tier 3: Complex (Dashboards, Multi-Step Workflows, Real-Time Interfaces)

#### Example 8: Logistics Dispatch Board
**What it is:** A real-time dispatch dashboard where operators assign drivers to routes, monitor delivery status, handle exceptions, and optimize scheduling.
**Why video adds value:** The dispatch board is a living interface -- statuses change, new orders appear, map positions update, alerts fire. Screenshots capture a frozen moment; video captures the rhythm of operations, the frequency of updates, and the operator's response patterns.
**Complexity:** High

#### Example 9: Trading Platform / Bloomberg Terminal Workflow
**What it is:** A financial trading interface with real-time data feeds, order entry, position monitoring, and risk management panels.
**Why video adds value:** Trading interfaces involve real-time data streaming, keyboard-driven command entry, and multi-panel layouts where information in one panel drives decisions in another. The Bloomberg Terminal's interface, barely changed in decades, uses a command-line paradigm (typing "AAPL Equity GO") that is unintelligible from screenshots alone.
**Complexity:** Very High

#### Example 10: Hospital EHR Clinical Workflow
**What it is:** A clinical workflow in a legacy EHR -- patient lookup, chart review, order entry, documentation, and discharge planning.
**Why video adds value:** Clinical workflows are safety-critical sequences where the order of operations matters (verify patient identity -> review allergies -> enter medication -> confirm dose -> sign order). Video captures the complete chain of custody for a clinical decision, including error prevention dialogs and confirmation steps.
**Complexity:** Very High

#### Example 11: Government Benefits Application Portal
**What it is:** A citizen-facing portal for applying for government benefits -- multi-page form with document upload, eligibility checks, and status tracking.
**Why video adds value:** Benefits applications involve complex eligibility branching (household size changes required documentation), progressive disclosure (only showing relevant sections), and status transitions (submitted -> under review -> approved/denied). Video captures the full applicant journey including edge cases.
**Complexity:** Medium-High

#### Example 12: AS/400 Green Screen Order Entry
**What it is:** A green-screen terminal application for entering and processing customer orders, used in manufacturing and distribution.
**Why video adds value:** Green screen navigation is entirely keyboard-driven with function keys, command codes, and menu hierarchies that are invisible in screenshots. Video captures the *exact sequence of keystrokes* and screen transitions that define the workflow.
**Complexity:** Medium (UI simple, workflow complex)

#### Example 13: Internal Analytics Dashboard (Legacy Tableau/Crystal Reports)
**What it is:** A corporate reporting dashboard with multiple chart types, drill-down capabilities, date range filtering, and export functionality.
**Why video adds value:** Dashboard interactions -- clicking a chart slice to drill down, adjusting date ranges to see data update, hovering for tooltips, switching between views -- are fundamentally temporal. The interactivity *is* the product.
**Complexity:** Medium-High

#### Example 14: Dental Practice Management Software
**What it is:** A legacy dental practice management system (Dentrix, Eaglesoft) with patient scheduling, charting, treatment planning, and insurance claims.
**Why video adds value:** Dental software has unique UI paradigms (tooth charting with click-to-annotate, treatment plan builders with drag-and-drop procedure ordering) that are domain-specific and difficult to describe in text. Video of a dental assistant scheduling a patient and creating a treatment plan communicates the workflow instantly.
**Complexity:** Medium

#### Example 15: Lotus Notes Approval Workflow
**What it is:** A custom Lotus Notes application for expense report approval -- submission, multi-level routing, comments, and notification.
**Why video adds value:** Notes approval workflows involve document state transitions (draft -> submitted -> manager review -> finance review -> approved/rejected), conditional routing (amounts over $5K require VP approval), and embedded rich text with attachments. The complete lifecycle is only visible in video.
**Complexity:** Medium-High

---

## 4. Persona Deep Dive: Coder vs Non-Coder

### 4.1 Technical Users (Coders)

**Profile:**
- Full-stack developers, frontend specialists, or freelance developers
- Comfortable with React, Vue, Next.js, or similar frameworks
- Currently use tools like Cursor, Copilot, v0, or bolt.new
- Working either at companies modernizing internal tools or as contractors hired to rebuild applications

**Current Workflow for Cloning/Recreating Apps:**
1. Take screenshots of the target application (maybe 5-20 static screenshots)
2. Open browser DevTools and inspect elements for CSS, layout, and component structure (if it is a web app)
3. Write a text prompt describing what they want ("build me a dashboard with a sidebar nav, a data table, and three KPI cards at the top")
4. Paste screenshots into v0, CopyCoder, or Lovable to generate initial code
5. Iterate extensively -- the generated output captures maybe 60-70% of the design, missing interaction patterns, state management, responsive behavior, and edge cases
6. Manually code the remaining 30-40%

**Pain Points That Video-to-Spec Solves:**
- **Interaction documentation gap:** Screenshots don't capture hover states, transitions, loading sequences, or conditional UI changes. Developers currently either guess or do extensive manual testing of the original app.
- **Multi-step workflow amnesia:** After taking 20 screenshots, it is hard to remember which screen follows which and what triggers the transitions. Video preserves the complete flow graph.
- **State management blindness:** The same screen can look different depending on user role, data state, or prior actions. Screenshots show one variant; video can show multiple.
- **Client communication overhead:** When developers are hired to "rebuild something like X," the back-and-forth to clarify what "like X" means consumes 20-30% of project time.

**Desired Output:**
- **Code output** (React/Next.js components, Tailwind CSS) is strongly preferred
- Component-level breakdown with props and state management
- API schema suggestions inferred from the data visible in the screencast
- Routing structure derived from the navigation observed in video

**Willingness to Pay:**
Developers already pay $20-100/month for tools like Cursor, Copilot, v0, and Lovable. A video-to-code tool that saves 5-10 hours per project at $50-150/hour consulting rates creates clear ROI at $30-100/month.

### 4.2 Non-Technical Users (Non-Coders)

**Profile:**
- Product managers, startup founders, entrepreneurs, agency owners, business analysts
- Cannot code but have strong opinions about what they want
- Currently use Figma (at a basic level), Canva, or simply write text documents and send Loom recordings
- May hire developers on Upwork, Toptal, or through dev agencies

**Current Workflow for Communicating "Build Me Something Like X":**
1. Find an app they admire -- maybe a competitor, maybe an internal tool at their previous company
2. Take scattered screenshots on their phone or via Loom
3. Write a Notion doc or Google Doc attempting to describe what they want: "It should have a sidebar like Notion, a kanban board like Trello, and the onboarding flow should be like Linear"
4. Include rough wireframes drawn in Figma, Miro, or even PowerPoint
5. Hand this to a developer or agency, who interprets it with varying accuracy
6. Endure 3-5 rounds of revision because the spec was ambiguous

Industry data confirms this pain: poor communication and unclear requirements cause up to 30% of development delays. The fundamental issue is that non-technical users think in terms of *experiences* ("it should feel snappy," "the transition should be smooth") while specifications require *precision* ("200ms ease-in-out transition on the card component, triggered by hover state").

**Pain Points That Video-to-Spec Solves:**
- **The vocabulary gap:** Non-technical users do not know terms like "accordion component," "skeleton loader," "infinite scroll," or "debounced search." They can *show* what they mean but cannot *name* it.
- **The "lost in translation" problem:** 30% of development delays stem from unclear requirements. Video captures intent without requiring technical vocabulary.
- **The multi-tool fatigue:** Currently, communicating a design idea requires Figma + Notion + Loom + screenshots + meetings. A single screencast-to-spec tool collapses this stack.
- **The cost of ambiguity:** Each round of revision with an outsourced developer costs time and money. A detailed spec generated from video reduces revision cycles.

**Desired Output:**
- **PRD (Product Requirements Document)** is the primary output -- something they can hand to any developer or agency
- Annotated wireframes showing the UI structure observed in the video
- User flow diagrams extracted from the navigation patterns
- Interaction specifications (what happens when you click X, hover over Y, submit Z)
- Optionally, a functional prototype they can click through to validate before sending to developers

**Willingness to Pay:**
Non-technical founders are accustomed to paying $50-500 for tools that save them from hiring expensive help earlier (Figma, Webflow, Notion, etc.). A tool that replaces $5,000-$20,000 in agency discovery/specification work would find strong adoption at $50-200/month. Individual PRD generations could also be priced per-use at $10-50 per video analysis.

### 4.3 The Right Equilibrium

**The Case for Serving Both:**
The tool's core technology -- video understanding -- is the same for both personas. The differentiation is in the *output format*:
- For coders: Code components, API schemas, routing structures
- For non-coders: PRDs, wireframes, flow diagrams, interaction specs

This is a classic "same engine, different interface" product architecture.

**The Case for Picking One:**
Lovable's meteoric growth ($7M to $206M ARR in one year, $6.6B valuation) proves that the non-technical user market is enormous and underserved. Fewer than 1% of people globally possess the skills to develop software independently. The non-coder persona represents a *much* larger addressable market.

However, the coder persona represents easier initial adoption -- developers are early adopters, have credit cards ready, and can evaluate the tool's quality immediately. CopyCoder/Komposo has already reached 100,000+ users by targeting this audience.

**Recommended Strategy:**
1. **Launch targeting coders** -- they are easier to reach (dev Twitter, Product Hunt, Hacker News), faster to convert, and their feedback will improve the core technology
2. **Expand to non-coders within 6-12 months** -- once the video understanding is polished, add PRD/wireframe output modes and market through entrepreneur/PM communities
3. **The non-coder market is the long-term prize** -- it is 100x larger and less competitive than the developer tools space

### 4.4 Market Sizing Intuition

| Dimension | Coder Persona | Non-Coder Persona |
|-----------|---------------|-------------------|
| **Global population** | ~30M professional developers | ~500M+ knowledge workers who need software built |
| **Current tool spending** | $20-100/month (Cursor, Copilot, v0) | $0-50/month (Figma, Notion) |
| **Problem severity** | Moderate (saves time, not essential) | Severe (cannot accomplish task without help) |
| **Price sensitivity** | Medium (comparison shops tools) | Low (compares to hiring developers at $100+/hr) |
| **Adoption speed** | Fast (self-serve, immediate evaluation) | Slow (needs onboarding, trust-building) |
| **Retention** | Medium (switches to next hot tool) | High (if it works, it becomes essential) |
| **Revenue potential** | $50-100/month ARPU | $100-300/month ARPU (or per-project pricing) |

The non-coder persona represents a larger long-term opportunity, but the coder persona is the faster path to product-market fit and initial revenue.

---

## 5. The App Cloning Workflow

### 5.1 Ideal User Journey: Screencast to Working App

```
Step 1: RECORD
User records a screencast of the target application
(2-10 minutes, narrating their workflow)
         |
         v
Step 2: UPLOAD & ANALYZE
Merleau processes the video using Gemini's video understanding
- Identifies UI components (buttons, forms, tables, navigation)
- Extracts user flow (sequence of screens, transitions)
- Recognizes interaction patterns (clicks, hovers, scrolls, drags)
- Detects state changes (loading states, error states, success states)
- Transcribes narration for context and intent
         |
         v
Step 3: GENERATE SPECIFICATION
Merleau produces structured output:
- Component inventory (every UI element identified)
- User flow diagram (screens + transitions)
- Interaction specification (events + responses)
- Data model inference (what data appears on screen, relationships)
- Visual design tokens (colors, typography, spacing)
         |
         v
Step 4: OUTPUT (persona-dependent)
FOR CODERS:                      FOR NON-CODERS:
- React/Next.js components       - PRD document
- Tailwind CSS styles            - Annotated wireframes
- Routing structure              - User flow diagrams
- API schema suggestions         - Interaction specs
- State management outline       - Clickable prototype
         |                                |
         v                                v
Step 5: ITERATE
User refines output:
- "Make the sidebar collapsible"
- "Add a dark mode toggle"
- "Change the data table to a kanban view"
         |
         v
Step 6: BUILD / HAND OFF
Coder: Imports into Cursor/IDE    Non-coder: Sends to dev team
and continues development         with complete specification
```

### 5.2 Where Video Understanding Adds the Most Value

Video understanding is not just "screenshots over time." It captures fundamentally different information than static images or text descriptions. The following analysis maps where video provides unique, irreplaceable value versus where screenshots or text might suffice.

#### Information Only Video Can Capture

| Capability | What It Reveals | Why Screenshots Cannot |
|-----------|----------------|----------------------|
| **Transitions and animations** | Fade-ins, slide-outs, accordion expansions, modal appearances, page transitions | Screenshots are frozen; animation is inherently temporal |
| **User flow and navigation** | The sequence of screens, the navigation path, branching decisions | Screenshots show individual screens but not the graph that connects them |
| **Timing and responsiveness** | Loading spinner duration, debounce delays on search, animation timing curves | No temporal data exists in screenshots |
| **State changes** | How the UI responds to actions -- a button changing from "Submit" to "Submitting..." to "Submitted" | Each state would require a separate screenshot, and the causal chain is lost |
| **Hover states and micro-interactions** | Tooltip appearances, button color changes on hover, dropdown menu opening | These states vanish the moment you take a screenshot (or appear artificially) |
| **Responsive behavior** | How the layout reflows when the browser is resized, breakpoint transitions | Would require multiple screenshots at arbitrary widths with no sense of the reflow behavior |
| **Error handling flows** | What happens when validation fails, when a network request times out, when a user enters invalid data | Error states are edge cases that are rarely captured in static documentation |
| **Real-time updates** | Live data feeds, notification badges incrementing, chat messages appearing | Static images cannot represent continuous data flow |
| **Keyboard shortcuts and power-user flows** | Tab order, keyboard navigation, shortcut key behavior | Invisible in any visual medium without motion |
| **Audio narration (with Gemini)** | The user explains *intent* while demonstrating -- "I click here because the client needs to see their balance first" | Text annotations on screenshots are an afterthought; narration is natural and rich |

#### Where Screenshots Suffice

- Static layouts with no interactivity (landing pages, about pages)
- Visual design details (exact colors, typography, spacing) -- though video can capture these too
- Single-state forms with no conditional logic

#### Where Text Descriptions Suffice

- High-level product concepts ("We need a project management tool")
- Business logic rules that are not reflected in UI ("Orders over $500 require manager approval")
- Non-visual requirements (performance, security, accessibility)

### 5.3 The Merleau Advantage: Video-First in a Screenshot-First World

The current competitive landscape is dominated by screenshot-to-code tools:

| Tool | Input | Output | Limitation |
|------|-------|--------|------------|
| **v0 (Vercel)** | Text prompt or single screenshot | React components | Single-screen, no flow understanding |
| **bolt.new** | Text prompt | Full-stack app | No visual input understanding |
| **Lovable** | Text prompt | Full-stack app | No visual input understanding |
| **CopyCoder/Komposo** | Screenshots (multi-image) | Structured prompt for AI IDEs | Static only, no interaction capture |
| **Figma Make** | Figma designs | Code components | Requires Figma file, not the running app |
| **Merleau (proposed)** | **Video/screencast** | **Spec, code, or PRD** | **Captures everything above** |

Merleau's video-first approach is a category-creating differentiator. No existing tool in the market takes *video of a running application* as input and produces a complete specification or codebase as output. This is not an incremental improvement over screenshot-to-code -- it is a fundamentally different capability enabled by Gemini's video understanding.

**Key technical enablers:**
- Gemini 2.5 Pro achieves state-of-the-art performance on video understanding benchmarks (84.8% on VideoMME)
- Gemini 2.5 can process audio-visual information seamlessly with code and other data formats
- Moment retrieval capabilities allow precise identification of specific segments within videos
- Gemini 2.5 Pro ranks #1 on the WebDev Arena leaderboard for building web apps

---

## 6. Strategic Recommendations

### 6.1 Highest-Value Target Segments (Prioritized)

1. **Internal tools and admin dashboards** -- Largest volume, least emotional attachment to existing design, fastest sales cycle
2. **Insurance and financial services legacy UIs** -- High willingness to pay, acute modernization pressure, complex workflows that showcase video's advantage
3. **SaaS cloning for entrepreneurs** -- Viral potential ("I cloned Notion in 5 minutes"), large market, low friction adoption
4. **Government legacy system modernization** -- Massive contracts but long sales cycles; better as a year-2 target
5. **Healthcare EHR modernization** -- Highly regulated but enormous TAM; requires compliance features

### 6.2 Go-to-Market Sequencing

**Phase 1 (Months 1-6): Developer-focused launch**
- Target: Developers using Cursor, v0, bolt.new, Lovable
- Input: Screencast video
- Output: React components + Tailwind CSS + routing structure
- Channel: Dev Twitter, Product Hunt, Hacker News, YouTube tutorials
- Pricing: Freemium with 3 free video analyses/month, $30-50/month pro

**Phase 2 (Months 6-12): Non-coder expansion**
- Target: Product managers, founders, agency owners
- Input: Same screencast video
- Output: PRD document + wireframes + flow diagrams
- Channel: Indie Hackers, entrepreneur communities, PM newsletters
- Pricing: $50-100/month or $25-50 per analysis

**Phase 3 (Months 12-24): Enterprise legacy modernization**
- Target: Enterprise IT teams modernizing SAP, Oracle Forms, AS/400
- Input: Screencast of legacy application workflows
- Output: Complete specification + recommended architecture + code scaffolding
- Channel: Direct sales, partnerships with modernization consultancies
- Pricing: $500-2000/month per team or project-based pricing

### 6.3 Key Differentiator to Emphasize

The core messaging should center on a simple insight:

> "Screenshots show you what an app looks like. Video shows you how an app works."

Every competitor in the space takes screenshots as input. Merleau takes video. This is not a marginal improvement -- it is the difference between capturing a *design* and capturing a *product*. Designs are layouts and colors. Products are workflows, interactions, state changes, and user journeys. Video captures all of these. Screenshots capture none of them.

---

## Sources

- [Legacy App Modernization: Best Practices & Approaches for 2026 (MobiDev)](https://mobidev.biz/blog/legacy-application-modernization-approaches-strategy-case-studies)
- [Application Modernization Services Market Size Report, 2034 (Polaris)](https://www.polarismarketresearch.com/industry-analysis/application-modernization-services-market)
- [Legacy Software Modernization Service Market Analysis 2035 (WiseGuy)](https://www.wiseguyreports.com/reports/legacy-software-modernization-service-market)
- [SAP, Salesforce Lead $356B Enterprise Applications Market (CIO/IDC)](https://www.cio.com/article/2496985/sap-salesforce-lead-356-billion-enterprise-applications-market-idc.html)
- [Why Some Users Hate Their SAP UI/UX (Eursap)](https://eursap.eu/blog/why-some-users-hate-their-sap-user-interface-user-experience-and-how-to-fix-it)
- [Oracle Forms Migration Planning 2025 (Patrick Hamou/Medium)](https://medium.com/@phamou/how-to-best-plan-for-your-oracle-forms-migration-in-2024-3f53eceae949)
- [Oracle Forms Migration to APEX (Pretius)](https://pretius.com/blog/oracle-forms-migration)
- [COBOL and the Government Mainframe Modernization Challenge (Karsun)](https://karsun-llc.com/blog/cobol-and-the-government-mainframe-modernization-challenge/)
- [GAO Report: Modernizing Critical Legacy Systems](https://www.gao.gov/products/gao-25-107795)
- [Outdated EHR & Legacy Systems: Hidden Risk to Patient Safety (ARG)](https://www.aresgrp.com/blog/legacy-ehr-modernization)
- [Legacy Healthcare Software Modernization Guide (Binariks)](https://binariks.com/blog/healthcare-software-modernization/)
- [From WinForms to Blazor: Modernizing Legacy .NET Apps (Softacom)](https://www.softacom.com/blog/migration/from-winforms-to-blazor-a-modernization-path-for-legacy-net-apps/)
- [Lotus Domino Migration Guide (Crow Canyon)](https://www.crowcanyon.com/blog/lotus-notes-migration-replacement-made-easy-with-nitro-studio/)
- [Lotus Notes Replacement: Rebuild for the 21st Century (OutSystems)](https://www.outsystems.com/blog/posts/lotus-notes-replacement/)
- [AS400 Green Screen Modernization FAQ (Integrative Systems)](https://www.integrativesystems.com/as400-green-screen-modernization-faq/)
- [Insurance Legacy System Transformation (Intellias)](https://intellias.com/insurance-legacy-system-transformation/)
- [How P&C Insurers Can Modernize Core Systems (McKinsey)](https://www.mckinsey.com/industries/financial-services/our-insights/how-p-and-c-insurers-can-successfully-modernize-core-systems)
- [Legacy TMS: When Yesterday's Software Holds Back Logistics (Amousin)](https://www.amousinternational.com/post/legacy-tms-when-yesterday-s-software-holds-today-s-logistics-back)
- [Real Estate Legacy Systems: Roadmap to Digital Transformation (Ascendix)](https://ascendixtech.com/real-estate-legacy-systems/)
- [Vibe Coding and How AI is Changing Who Can Build Apps (Microsoft)](https://news.microsoft.com/source/features/ai/vibe-coding-and-other-ways-ai-is-changing-who-can-build-apps-and-how/)
- [Vibe Coding: A Guide for Startups and Founders (JP Morgan)](https://www.jpmorgan.com/insights/technology/artificial-intelligence/vibe-coding-a-guide-for-startups-and-founders)
- [The 2025 State of Visual Development and Vibe Coding (Bubble)](https://bubble.io/blog/2025-state-of-visual-development-ai-app-building/)
- [Lovable Revenue, Funding & Growth Rate (Sacra)](https://sacra.com/c/lovable/)
- [Lovable Raises $330M Series B (TechCrunch)](https://techcrunch.com/2025/12/18/vibe-coding-startup-lovable-raises-330m-at-a-6-6b-valuation/)
- [CopyCoder: Transform Designs into Code with AI](https://www.copycoder.net/)
- [Clone Web Applications Using CopyCoder and Bolt.new (AI Tech Toolbox)](https://blog.aitechtoolbox.com/clone-web-applications-using-copycoder-and-bolt-new/)
- [Screenshot to Code: Lovable vs v0 vs Bolt in 2026 (AIMultiple)](https://research.aimultiple.com/screenshot-to-code/)
- [V0 vs Bolt.new vs Lovable Comparison 2026 (NxCode)](https://www.nxcode.io/resources/news/v0-vs-bolt-vs-lovable-ai-app-builder-comparison-2025)
- [Advancing Video Understanding with Gemini 2.5 (Google Developers Blog)](https://developers.googleblog.com/en/gemini-2-5-video-understanding/)
- [Video Understanding with Gemini API (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/video-understanding)
- [Reverse Engineering Applications with AI (Daffodil Software)](https://insights.daffodilsw.com/blog/reverse-engineering-applications-with-ai-from-ui-to-code-generation)
- [SeeHow: Workflow Extraction from Programming Screencasts (ACM/ICSE)](https://dl.acm.org/doi/10.1109/ICSE48619.2023.00165)
- [CodeSCAN: ScreenCast Analysis for Video Programming Tutorials (arXiv)](https://arxiv.org/abs/2409.18556)
- [ChatPRD: AI Platform for Product Managers](https://www.chatprd.ai/)
- [Low-Code Revolution 2025: Transforming Business with Retool](https://retoolers.io/blog-posts/low-code-revolution-in-2025-transforming-business-operations-with-retool)
- [Top 10 Low-Code Internal Tool Builders (ToolJet)](https://blog.tooljet.com/top-10-internal-tool-builders/)
- [Designer's Handbook for Developer Handoff (Figma)](https://www.figma.com/blog/the-designers-handbook-for-developer-handoff/)
- [Bloomberg Terminal Innovation (Bloomberg LP)](https://www.bloomberg.com/company/stories/innovating-a-modern-icon-how-bloomberg-keeps-the-terminal-cutting-edge/)
- [Transforming Legacy System for Logistics Leader (Clear Function)](https://www.clearfunction.com/case-study/case-study-legacy-code-to-modern-ux-overhauling-50-apps-for-a-logistics-powerhouse)
