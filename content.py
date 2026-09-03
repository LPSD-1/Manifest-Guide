# -*- coding: utf-8 -*-
"""Every word of the Manifest guide, in one place.

`build.py` turns this into the multi-page site, the search index and the
single-file download. Content lives here once so those three can never drift
apart -- the whole reason this is generated rather than hand-written.

Structure: PAGES is a list of pages; each page has SECTIONS; each section has an
id (used as the anchor and by search), a heading, and a body of plain HTML.

House style, taken from the app itself:
  - British English, no exclamation marks, no marketing superlatives.
  - Say what the thing does, then say what it costs or refuses.
  - Never claim a feature that has not been driven on a device.
"""

PRODUCT = "Manifest"
STUDIO = "Manifest Studio"
POLICY_URL = "https://lpsd-1.github.io/Manifest-Privacy-Policy/"

FIELD_TYPES = [
    ("text", "Free text over several lines."),
    ("string", "A single line."),
    ("markdown", "Formatted text — headings, bold, lists."),
    ("integer", "A whole number."),
    ("decimal", "A number with a fractional part."),
    ("fraction", "Imperial fractions, kept as fractions rather than converted."),
    ("percent", "A percentage."),
    ("range", "A low and a high value — a tolerance, or a working range."),
    ("currency", "An exact amount with its currency. Stored to the penny, never as a float."),
    ("dimensions", "Length, width and height together, with units."),
    ("boolean", "Yes, no, or not yet answered — three states, not two."),
    ("date", "A calendar date, with a date picker."),
    ("time", "A time of day."),
    ("datetime", "A date and a time together."),
    ("dateRange", "A start and an end — a hire period, a warranty."),
    ("yearMonth", "A month and a year, for things dated no more finely than that."),
    ("duration", "Hours and minutes. Entered in two boxes rather than typed as a code."),
    ("recurrence", "How often something repeats — a service interval."),
    ("enum", "One value from a list you define."),
    ("multiEnum", "Any number of values from a list you define."),
    ("hierarchicalEnum", "A list with a tree in it, where choosing narrows the next choice."),
    ("status", "A state with a colour, so it reads at a glance."),
    ("tags", "Free-form labels, reusable across the catalogue."),
    ("rating", "A score out of a maximum you set."),
    ("colour", "A colour, shown as a swatch."),
    ("email", "An address, checked for shape and tappable to write to."),
    ("phone", "A number, tappable to dial. Extensions are accepted."),
    ("url", "A web address, tappable to open."),
    ("link", "A web address with your own label on it."),
    ("person", "A name — an engineer, a customer, a signatory."),
    ("address", "A postal address in its proper parts, not one squashed line."),
    ("geoPoint", "A latitude and longitude. Shown and sorted; there is no map picker yet, so a value has to arrive in an imported catalogue."),
    ("storageLocation", "Where the thing physically lives — bay, shelf, van."),
    ("serial", "A serial number, in a monospaced face so 0 and O differ."),
    ("barcode", "A code that can be printed and scanned back."),
    ("nfcTag", "An NFC tag identifier, stored and shown as text. The app does not read or write tags itself; the identifier is typed or scanned in."),
    ("ref", "A pointer to another part in the same catalogue."),
    ("image", "A photograph. Offered on a part; not yet on a job form."),
    ("file", "An attached document — a datasheet, a certificate. No editor yet: a value has to arrive in an imported catalogue."),
    ("signature", "A signature drawn on the glass, on a job. Once given it cannot be altered, and it is deliberately not a part field."),
    ("audio", "A voice note, recorded through the phone's own recorder. Offered on a job; not yet on a part."),
    ("video", "A clip, recorded through the phone's own camera app. Offered on a job; not yet on a part."),
    ("array", "A repeating list of any of the above."),
    ("object", "A group of fields treated as one thing."),
]

TIERS = [
    ("Free", "None — one device, for trying it out", "Free"),
    ("Solo", "1", "£20"),
    ("Team", "10", "£70"),
    ("Fleet", "Any number", "£150"),
    ("Catalogue server", "Add-on — requires Team or Fleet", "£120"),
]

SAMPLES = [
    ("Vehicle workshop", "Parts by manufacturer, and what they fit"),
    ("Electrical contractor", "Stock by rating, and where it lives in the van"),
    ("Joinery and carpentry", "Timber by material, thickness and finish"),
    ("Plumbing and heating", "Fittings by pipe size and material"),
    ("Fire protection", "Equipment by extinguishing agent, with service dates"),
    ("Equipment hire", "Individual assets by tag, serial and condition"),
]


def field_type_table():
    rows = "\n".join(
        f"<tr><th scope='row'><code>{name}</code></th><td>{desc}</td></tr>"
        for name, desc in FIELD_TYPES
    )
    return (
        "<div class='scroll'><table class='ref'>"
        "<thead><tr><th scope='col'>Type</th><th scope='col'>What it holds</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


def tier_table():
    rows = "\n".join(
        f"<tr><th scope='row'>{t}</th><td>{h}</td><td class='num'>{p}</td></tr>"
        for t, h, p in TIERS
    )
    return (
        "<div class='scroll'><table class='price'>"
        "<thead><tr><th scope='col'>Tier</th><th scope='col'>Handsets you can pair</th>"
        "<th scope='col'>One-time</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


def sample_table():
    rows = "\n".join(
        f"<tr><th scope='row'>{t}</th><td>{d}</td></tr>" for t, d in SAMPLES
    )
    return (
        "<div class='scroll'><table>"
        "<thead><tr><th scope='col'>Trade</th><th scope='col'>Shaped around</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


PAGES = [
    # ------------------------------------------------------------------ index
    {
        "slug": "index",
        "title": "Overview",
        "blurb": "What Manifest is, who it is for, and the one idea behind it.",
        "sections": [
            {
                "id": "what",
                "heading": "What Manifest is",
                "body": """
<p><strong>Manifest</strong> is a parts catalogue and job sheet for people who
work with their hands. It runs on an ordinary Android phone, works with no
signal, and takes its entire shape — fields, categories, colours, even the words
on the buttons — from a document you control.</p>

<p>It comes as a pair of apps. <strong>Manifest</strong> is what the person on
the tools carries. <strong>Manifest Studio</strong> is where the catalogue is
built and the job forms are designed.</p>
""",
            },
            {
                "id": "idea",
                "heading": "The one idea",
                "body": """
<p>Most trade software gives you fixed fields and asks you to describe your
business in somebody else's vocabulary. You end up with a “Notes” column holding
the three things that actually matter.</p>

<p>Manifest works the other way round. One document carries your field
definitions, your categories, your appearance and your parts, and the app
assembles itself from that document. Change the document and the app changes on
every handset holding it.</p>

<div class="pull"><p>A joiner browses by material and thickness. A fire
contractor browses by extinguishing agent and service date. The same
application, unmodified — no plugins, no configuration consultant, no per-seat
fee.</p></div>
""",
            },
            {
                "id": "offline",
                "heading": "It works with no signal",
                "body": """
<p>Signal is worst exactly where the parts are: a plant room, a basement, a
loading bay, a site with no mast for a mile. Offline is not a mode you switch
on — it is the normal state.</p>

<p>Search, browse, scan a code, open a drawing, fill in a job sheet, take a
signature: all of it happens on the handset with nothing to reach. There is no
spinner waiting on a server, because there is no server. Where something
genuinely needs a network — fetching a catalogue update, sending a finished
job — it says so, and holds the work until there is one. It tries again the next
time somebody opens the app; nothing runs while the phone is in a pocket.</p>
""",
            },
            {
                "id": "who",
                "heading": "Who it suits",
                "body": """
<ul>
<li>A trade business with a parts list, a stores area or a van stock.</li>
<li>Anyone servicing equipment on site who has to record what was done.</li>
<li>Hire businesses tracking individual assets rather than models.</li>
<li>Anyone whose data does not fit the boxes their current software provides.</li>
</ul>

<p>It suits you less well if you need live stock quantities, scheduling and
dispatch, or accounts for individual users. <a href="pricing.html#not">What it
deliberately is not</a> covers that honestly.</p>
""",
            },
        ],
    },
    # ------------------------------------------------------------------ start
    {
        "slug": "start",
        "title": "Getting started",
        "blurb": "Installing the pair, the six worked examples, and your first hour.",
        "sections": [
            {
                "id": "two-apps",
                "heading": "The two apps",
                "body": """
<div class="cards">
  <div><h3>Manifest</h3><p>For the person on the tools. Browse, search, scan,
  open floor plans, fill in job sheets. It reads the catalogue rather than
  editing it, so nobody loses a week's authoring on a busy Friday.</p></div>
  <div><h3>Manifest Studio</h3><p>Everything above, plus authoring: build the
  catalogue, take photographs, mark up floor plans, design job forms, print
  labels, and hand the finished catalogue to your team.</p></div>
</div>

<p>Both can live on the same phone; in the launcher they appear as
<em>Manifest</em> and <em>Manifest Studio</em>. Studio asks for the phone's PIN,
pattern or fingerprint each time it opens, and will not run at all on a handset
with no screen lock — it holds your whole catalogue and the key your fleet
trusts.</p>
""",
            },
            {
                "id": "samples",
                "heading": "Start from a worked example",
                "body": """
<p>Six complete sample catalogues ship inside the app, one per trade, each with
forty parts, floor plans and assemblies. They exist to prove the claim on the
front page: they look nothing like each other, and they run unchanged in the
same application.</p>
"""
                + sample_table()
                + """
<p>The last is deliberately the odd one out. A hire business identifies the
<em>thing</em>, not the model — two identical speakers are two records, and the
title field is an asset tag rather than a part number. That is the same app with
a different idea of what a record even is.</p>

<div class="note"><p><strong>Choosing an example adopts it.</strong> It becomes
your own catalogue under your own identity, rather than staying a shared sample.
Your first five minutes are “delete what we don't stock” instead of “type in
five hundred parts”.</p></div>
""",
            },
            {
                "id": "first-hour",
                "heading": "A sensible first hour",
                "body": """
<ol>
<li>Install <strong>Manifest Studio</strong> and let it take you through the
credential prompt.</li>
<li>Load the sample nearest your trade, and browse it until the structure makes
sense.</li>
<li>Either edit that sample into your own catalogue, or
<a href="data.html#spreadsheet">import your existing spreadsheet</a> over the
top of it.</li>
<li>Set your <a href="catalogue.html#look">colours and logo</a> and your
<a href="catalogue.html#words">own words</a> for the sections.</li>
<li>Install <strong>Manifest</strong> on a second handset and
<a href="safety.html#pairing">pair it</a>.</li>
<li>Write your <a href="safety.html#recovery">recovery file</a> before you have
anything you would miss. Writing one is paid, because it takes your catalogue off
the handset; checking and restoring one are free on every tier.</li>
</ol>

<div class="warn"><p>Step six is the one people skip. A handset is a thing that
gets dropped, stolen and left on a roof, and there is no service holding a copy
for you.</p></div>
""",
            },
        ],
    },
    # -------------------------------------------------------------- catalogue
    {
        "slug": "catalogue",
        "title": "Your catalogue",
        "blurb": "Fields, structure, your own words, appearance, and getting a catalogue built quickly.",
        "sections": [
            {
                "id": "fields",
                "heading": "Fields",
                "body": """
<p>A record carries whatever your trade needs it to. There are <strong>44 field
types</strong>, and each one knows what it is — so a date gets a date picker, a
duration gets hours and minutes, money is stored as an exact amount with its
currency rather than a rounded number, a phone number dials, and a link opens.</p>

<p>For each field you decide the label, whether it is required, whether it is
searchable and how heavily it is weighted against other fields at the same rank,
where it appears on the part page,
and any bounds it must respect.</p>

<p>The full list is in the <a href="reference.html#types">field type
reference</a>.</p>
""",
            },
            {
                "id": "structure",
                "heading": "Structure",
                "body": """
<p>You decide how parts are grouped and how deep the tree goes — by category, by
location, by rating, by whatever your trade actually uses to find things. A
catalogue can be browsed on more than one axis at once, so the same stock can be
reached by category and by where it lives.</p>

<p>Tapping a value on a part page — a manufacturer, a rating, a tag — narrows the
list to everything sharing it, and shows as a chip you can remove. Sections are
the durable version of the same idea: they come from a field's values, so the
catalogue organises itself and there is no second structure to keep in step.</p>
""",
            },
            {
                "id": "words",
                "heading": "Your own words",
                "body": """
<p>The app's own section names are yours. A <strong>Build</strong> can be a Kit,
an Assembly, a Rig or a Job Pack. <strong>Plans</strong> can be Sites or
Drawings. A <strong>Job</strong> can be a Visit, a Service or a Call.</p>

<p>These are not translations. They are your nouns, carried inside your
catalogue, so the identical installed app uses different words on different
companies' handsets — including in menus, empty states and confirmation
messages.</p>
""",
            },
            {
                "id": "look",
                "heading": "Appearance",
                "body": """
<p>Your colours and your logo travel in the catalogue, so the app on your team's
phones looks like your company rather than like ours. Light and dark are both
handled, and the colours are checked for contrast so a brand colour cannot make
text unreadable.</p>
""",
            },
            {
                "id": "ai",
                "heading": "Converting an existing list with AI",
                "body": """
<p>Studio can export a <strong>schema for AI conversion</strong>: a description
of your catalogue's structure, with no parts and no prices in it.</p>

<p>Send that to any AI assistant along with your own parts list — in whatever
shape it happens to be, however inconsistent — and it will give you back a file
Manifest can import. It is the fastest route from a twenty-year-old spreadsheet
to a working catalogue.</p>

<p>You can also export the schema alone to set up a second catalogue with the
same shape as the first.</p>
""",
            },
            {
                "id": "quality",
                "heading": "Catalogue quality",
                "body": """
<p>Studio can review the catalogue and report what looks wrong or unfinished —
the sort of thing that is invisible while you are typing and obvious to somebody
using it in a van three weeks later.</p>
""",
            },
            {
                "id": "many",
                "heading": "More than one catalogue",
                "body": """
<p>A business can hold several catalogues on one Studio — one per area of the
business, or one per site — and move between them. Each is separate: its own
fields, its own parts, its own appearance.</p>
""",
            },
        ],
    },
    # ---------------------------------------------------------------- working
    {
        "slug": "working",
        "title": "On the floor",
        "blurb": "Browsing, search, scanning, floor plans, assemblies and your own private notes.",
        "sections": [
            {
                "id": "browse",
                "heading": "Browsing and the part page",
                "body": """
<p>Parts are listed densely, because a person holding a phone in a cold plant
room wants to see ten of them, not two. Part numbers are set in a monospaced
face so <code>0</code> and <code>O</code> cannot be confused when you are
ordering one.</p>

<p>A part page shows every field you defined, in the order and grouping you
chose, with photographs and any references to other parts.</p>
""",
            },
            {
                "id": "search",
                "heading": "Search",
                "body": """
<p>Every area has a search bar, and it sits within thumb reach rather than at
the top of the screen where a one-handed grip cannot get to it.</p>

<p>Search covers the fields you marked searchable. Identifiers rank first — an
exact match, then a match at the start, then one anywhere inside — and
descriptions and other fields come after those. A weight you set breaks ties
within one of those bands. Results appear as you type, and a row says which field
matched.</p>
""",
            },
            {
                "id": "scan",
                "heading": "Scanning",
                "body": """
<p>Point the camera at a QR code or a barcode and land directly on that part.
The scanner reads 2D codes and ordinary 1D barcodes.</p>

<p>Scanning also <strong>fills fields in</strong>: a job sheet asking for a
panel serial can have it scanned in rather than typed with gloves on. Codes a
manufacturer already prints can be adopted, so you do not have to relabel stock
that already carries a usable code.</p>
""",
            },
            {
                "id": "plans",
                "heading": "Floor plans",
                "body": """
<p>Drop your site drawings in, mark out the zones, and place parts on the map.
Tap a zone to see everything in it, and go straight from the map to a part
page.</p>

<p>It earns its keep the first time somebody is sent to a building they have
never been to, and needs to find the panel before they can start.</p>
""",
            },
            {
                "id": "builds",
                "heading": "Builds and assemblies",
                "body": """
<p>Group parts into the things you actually book out or install as a unit — an
assembly, a kit, a rig, a job pack. Select several parts at once and add them to
a build in one action.</p>
""",
            },
            {
                "id": "selecting",
                "heading": "Doing something to several parts at once",
                "body": """
<p>Select a run of parts — or everything in a zone, in one action — and then act
on the selection: print labels for all of them, or add them all to a build.</p>

<p>It is the difference between labelling a stores area in an afternoon and
labelling it one part at a time.</p>
""",
            },
            {
                "id": "photos",
                "heading": "Photographs",
                "body": """
<p>A part can carry photographs, taken with the phone or picked from the
gallery. They are compressed on the way in and travel with the catalogue in a
bundle, so a handset with no signal still has the picture.</p>

<p>Parts can also point at other parts, so a fitting can name what it fits and
you can move between them.</p>
""",
            },
            {
                "id": "myparts",
                "heading": "My parts",
                "body": """
<p>Anyone can mark parts as their own favourites and attach a private note to a
part — what you know about it, what it actually fits, which supplier is
reliable.</p>

<div class="note"><p>Favourites and notes stay <strong>on that phone</strong>.
They are not part of the catalogue and they are not sent anywhere, so an
engineer's own working knowledge is theirs and does not travel with an
export.</p></div>
""",
            },
        ],
    },
    # ------------------------------------------------------------------- jobs
    {
        "slug": "jobs",
        "title": "Jobs",
        "blurb": "Designing job sheets, filling them in on site, and getting completed work off the handset.",
        "sections": [
            {
                "id": "forms",
                "heading": "The job sheet is a form you designed",
                "body": """
<p>A job form is built from the same field types as the rest of the catalogue and
lives in your catalogue. Most are offered on a job — a signature, a voice note, a
video clip, a duration or an address as readily as a line of text. Three are not
offered on a job yet: a photograph, a status with set steps, and a choice that
narrows as you pick. A form that already carries one keeps working. Whatever your trade records — visit type, devices tested,
defects found, outcome, next service date, invoice total — is a field you
defined, not a box we guessed at.</p>

<p><strong>Templates</strong> mean a recurring visit starts half filled in. An
annual service and a callback can be different forms.</p>
""",
            },
            {
                "id": "onsite",
                "heading": "Filling one in on site",
                "body": """
<div class="spec">
  <div><p class="k">Time</p><div class="v"><p>A timer runs while the work does,
  so time on site is recorded rather than remembered back at the van. It writes
  into a duration field you nominate, so put one on the form first, and it keeps
  running while the app is closed.</p></div></div>
  <div><p class="k">Recordings</p><div class="v"><p>A voice note or a video clip,
  through the phone's own recorder or camera app. Photographs are a
  <strong>part</strong> field today rather than a job field; a job form cannot
  yet ask for one.</p></div></div>
  <div><p class="k">Signatures</p><div class="v"><p>Captured on the glass. Once
  given, a signature cannot be quietly changed — which is the entire point of
  having one.</p></div></div>
  <div><p class="k">Parts used</p><div class="v"><p>Picked from the catalogue
  through the same search as the rest of the app, so a fitted part resolves to a
  real record rather than a typed string that nobody can reconcile
  later.</p></div></div>
  <div><p class="k">Scanning</p><div class="v"><p>Serials and asset tags can be
  scanned straight into their fields.</p></div></div>
</div>
""",
            },
            {
                "id": "completing",
                "heading": "Completing and reopening",
                "body": """
<p>A job is marked complete when the work is done. Required fields must be
answered first — the form refuses rather than silently saving a half-finished
record.</p>

<p>A completed job can be reopened if something was missed. Deleted jobs go to a
bin and stay recoverable for seven days.</p>
""",
            },
            {
                "id": "sending",
                "heading": "Getting completed work off the handset",
                "body": """
<p>A finished job can be sent automatically, to as many destinations as you
like. You configure these once in Studio and they travel to the fleet with the
catalogue, arriving <strong>working</strong> — switched on as you left them,
with no step at the far end, so handsets begin sending as soon as they load the
catalogue. If you want to try one van first, narrow the destination to named
handsets before you publish.</p>

<div class="scroll"><table>
<thead><tr><th scope="col">Destination</th><th scope="col">What it is for</th></tr></thead>
<tbody>
<tr><th scope="row">A folder</th><td>A shared drive or a watched folder,
<strong>on the Studio only</strong>. The folder permission belongs to the device
that chose the folder, so engineers' handsets skip a folder destination rather
than queueing work they could never deliver — the app says so where you pick it.
It needs no connectivity at all. Handsets send over a web address or by
email</td></tr>
<tr><th scope="row">A web address</th><td>Your own system, your CRM, a webhook.
Choose the body format and map your fields to whatever names the far end
expects</td></tr>
<tr><th scope="row">Email</th><td>Straight to the service desk. Email cannot
confirm delivery, and the app says so where you choose it</td></tr>
</tbody></table></div>

<p>Body formats for a web destination: <strong>JSON</strong>,
<strong>CSV</strong>, <strong>XML</strong>, <strong>form fields</strong> or
<strong>JSON lines</strong>. Sign-in is supported in several shapes, including
bearer tokens, API keys, basic authentication and signed requests.</p>
""",
            },
            {
                "id": "control",
                "heading": "Control over what leaves, and when",
                "body": """
<ul>
<li><strong>A field mapping</strong> decides exactly which values are sent and
what each is called at the other end. If a destination also attaches
photographs or signatures, the screen lists those separately rather than letting
a mapping imply it is the whole story.</li>
<li><strong>Send a test</strong> sends a sample completion so you can see it
arrive.</li>
<li><strong>Show the request</strong> displays precisely what would leave the
handset, before any real job does.</li>
<li><strong>A send window</strong> holds work until working hours.</li>
<li><strong>Wi-fi only</strong> holds work until the handset is off mobile
data.</li>
<li><strong>Named handsets</strong> can be the only ones that send to a given
destination, for a pilot.</li>
</ul>

<p>Anything not yet sent is listed plainly under <em>Waiting to send</em>, with
the reason. Nothing is deleted for having been sent unless you asked for that
explicitly.</p>
""",
            },
            {
                "id": "templates",
                "heading": "Templates",
                "body": """
<p>A template is a job form with some of it already answered. An annual service,
a callback, a commissioning visit and a remedial can each be their own template,
so the engineer picks one at the start and begins with the right fields in front
of them rather than the same blank form every time.</p>

<p>Templates live in the catalogue, so changing one changes it for the whole
fleet at the next catalogue update.</p>
""",
            },
            {
                "id": "byfile",
                "heading": "Moving jobs by file",
                "body": """
<p>Jobs can be exported to a file and imported on another handset. That is the
route for a business with no destinations configured at all: the work is done on
a phone, the file is handed over, and it opens on the machine that needs it —
with the photographs and signatures intact.</p>

<p>It is also how work gets off a handset that is about to be replaced.</p>
""",
            },
            {
                "id": "retention",
                "heading": "How long jobs are kept",
                "body": """
<p>You can set how long completed jobs stay on a handset, and separately how
long before the personal details in them are <strong>anonymised</strong>.
Anonymising always comes before deleting, so a record can lose the customer's
name and signature while the engineering facts stay.</p>

<p>Leave either empty and nothing happens on that schedule.
<strong>Retention deletes for good — it is not the seven-day bin.</strong> The
bin is for jobs somebody deletes by hand, which stay recoverable for seven
days.</p>

<div class="note"><p>The clock does not run on work that has not been sent yet.
A job waiting for a destination is not quietly deleted out from under you
because a retention period elapsed.</p></div>
""",
            },
            {
                "id": "inbound",
                "heading": "Work arriving from elsewhere",
                "body": """
<p>Jobs can travel the other way. Point the app at an <strong>https address you
control</strong> — your own scheduler or dispatch board — and each handset gets a
<strong>Fetch</strong> row on its Jobs tab that brings down what has been
assigned to it. It checks when that tab is opened; nothing polls in the
background. Fetching again reconciles the list rather than duplicating it. The
address, the credential and whatever comes back are yours; we never see any of
it.</p>
""",
            },
        ],
    },
    # ----------------------------------------------------------------- labels
    {
        "slug": "labels",
        "title": "Labels",
        "blurb": "Printing codes that scan back to the exact record, on stock you already buy.",
        "sections": [
            {
                "id": "printing",
                "heading": "Printing labels",
                "body": """
<p>Print a QR or barcode label for a part, stick it on the shelf, the bin or the
asset, and scanning it later opens that exact record.</p>

<p>Select any number of parts — a whole zone at once, if you like — choose your
stock, and Manifest lays out the sheet and renders a PDF. It tells you how many
labels, how many to a page and how many pages before it prints anything. A part
with no part number has no code to print, so it is left out — and you are told
how many, before any paper is spent.</p>
""",
            },
            {
                "id": "stocks",
                "heading": "Label stocks",
                "body": """
<p>Manifest knows the layout of <strong>34 label stocks</strong>:</p>

<ul>
<li><strong>Plain paper</strong> — A4, A5 and Letter.</li>
<li><strong>Avery</strong> — including L7160, L7161, L7163, L7165, L7169, L7651,
5160 and 5163.</li>
<li><strong>Brother</strong> — the DK die-cut and continuous rolls, and TZe
tape.</li>
<li><strong>Dymo</strong> — the common LabelWriter sizes and D1 tape.</li>
<li><strong>Zebra</strong>.</li>
</ul>

<p>The output is an ordinary PDF, so it goes to any printer you already have,
including the small thermal ones. Reprinting a single lost label does not mean
reprinting the sheet.</p>
""",
            },
        ],
    },
    # ------------------------------------------------------------------- data
    {
        "slug": "data",
        "title": "Getting data in and out",
        "blurb": "Spreadsheet import, exports, distributing to a fleet, the catalogue server and updates.",
        "sections": [
            {
                "id": "spreadsheet",
                "heading": "Importing a spreadsheet",
                "body": """
<p>Almost every business already has its parts in a spreadsheet. Studio imports
<strong>CSV and Excel</strong> files with a column mapping step: it reads your
headings, works out what each column is and what type it holds, and lets you
correct it.</p>

<p>It handles the things that usually break an import — a heading row that is
not the first row, mixed date formats, currency symbols, decimal commas — and it
tells you exactly what it is about to do before it does it:</p>

<div class="note"><p><code>5 to add, 0 to update, 0 rows skipped, 0 cells left
empty</code> — and then, plainly, <code>5 added, 0 changed, 40 removed</code>.
You see the removals before you agree to them.</p></div>

<p>You can <strong>replace</strong> a catalogue outright, or <strong>merge</strong>
a newer price list into the one you already have without doubling anything
up.</p>
""",
            },
            {
                "id": "exports",
                "heading": "Exporting your catalogue",
                "body": """
<div class="scroll"><table>
<thead><tr><th scope="col">Route</th><th scope="col">What it means</th></tr></thead>
<tbody>
<tr><th scope="row">Plain export</th><td>An ordinary readable file. Your data,
yours to keep, openable by anything. Stored credentials — passwords, keys,
tokens — are stripped out of it. <strong>A secret written into an address
cannot be</strong>: for a webhook the address <em>is</em> the credential, so a
destination URL travels as it stands. Studio says so where you author
one</td></tr>
<tr><th scope="row">Sealed export</th><td>Encrypted to the specific handsets you
name. Only those devices can open it</td></tr>
<tr><th scope="row">Bundle</th><td>The catalogue together with its photographs
and drawings, in one archive</td></tr>
<tr><th scope="row">Catalogue server</th><td>Handsets fetch updates themselves
over your own network</td></tr>
</tbody></table></div>

<p>Exports are named after the catalogue and the date, so a folder of them can
be read at a glance.</p>

<div class="note"><p><strong>There is no lock-in.</strong> The plain export is a
readable document you can keep, archive or move elsewhere. That is deliberate: a
format only our software can read would be lock-in wearing a security
badge.</p></div>
""",
            },
            {
                "id": "server",
                "heading": "The catalogue server",
                "body": """
<p>An optional extra for larger fleets. Studio exports a small, ready-to-run
program for <strong>Windows, Linux or a Raspberry Pi</strong>, together with its
configuration and its key.</p>

<p>Put it on a machine in your building, and every handset is offered new
catalogues over your own network the next time the app is opened on it — no web
host, no hosting bill, nothing exposed to the internet.</p>

<h3>What it does and refuses</h3>
<ul>
<li>The connection is <strong>pinned</strong>: handsets accept that one machine
and no other, so nothing on the network can impersonate it.</li>
<li>It <strong>refuses any request</strong> that does not carry the shared secret
it was issued with.</li>
<li>It will not serve its own key, will not list a directory, and serves nothing
except the catalogue.</li>
<li>It mints its own certificate on first run. There is nothing to configure and
no certificate to buy.</li>
</ul>

<p>Once bought, <em>Export catalogue server</em> appears in Studio under
Menu ▸ Catalogue. Before it is bought the row is absent rather than greyed
out, because a permanently dead control is an advertisement wearing a control's
clothes.</p>
""",
            },
            {
                "id": "updates",
                "heading": "Catalogue updates",
                "body": """
<p>A catalogue can name an address it updates from — your catalogue server, or
any https address you control. Handsets check on their own — but only when
somebody opens the app. Nothing runs in the background, so a phone left in a
drawer stays on the catalogue it has until it is next opened. Checking more
often than every fifteen minutes is ignored.</p>

<div class="note"><p><strong>An update is offered, never applied behind
somebody's back.</strong> A fetched catalogue goes through the same preview,
signature check and confirmation as a file handed over by hand — mid-shift, on
somebody's phone, is not the moment to change what the app says.</p></div>

<p>A source offering an older catalogue than the handset already holds is
refused, and the message says who has to act.</p>
""",
            },
        ],
    },
    # ----------------------------------------------------------------- safety
    {
        "slug": "safety",
        "title": "Fleet, backup and privacy",
        "blurb": "Pairing handsets, the recovery file, and what we can and cannot see.",
        "sections": [
            {
                "id": "pairing",
                "heading": "Pairing handsets",
                "body": """
<p>Handsets are paired to a Studio in person or over a phone line. Each device
shows a code, and you confirm the fingerprint matches — reading it out loud to
whoever is holding the other handset is enough. That check is the only thing
proving the request came from the device you think it did. From then on that
handset trusts catalogues that Studio has signed.</p>

<p>Checking the code is the step that matters: it is the only thing proving the
request came from the device in front of you, rather than from somebody else
entirely. Several handsets can be paired in one go from a folder of requests, and
each one is still confirmed individually.</p>

<p>A handset that is wiped and set up again can be paired again without spending
a second slot from your allowance.</p>
""",
            },
            {
                "id": "recovery",
                "heading": "The recovery file",
                "body": """
<p>A phone is a thing that gets dropped, stolen and left on a roof. So Studio
writes a <strong>recovery file</strong>: one encrypted file holding your Studio
identity, your catalogue, the key your fleet trusts, and the photographs and
signatures attached to jobs. <strong>The catalogue's own part photographs are
deliberately not in it</strong> — packing every part image into one envelope
makes a file too large to be worth having. They travel in a catalogue
<strong>bundle</strong> instead, so keep a bundle beside the recovery file and
between them everything is covered.</p>

<p>Restore it on a new phone and that phone <strong>is</strong> your Studio. The
handsets you already paired carry on working, with nothing to redo at their
end.</p>

<div class="warn"><p>It is encrypted with a passphrase you choose, and
<strong>we cannot recover it</strong>, because we never have it. There is no
service, no reset link and no back door. Write the passphrase down somewhere
that is not the phone.</p></div>

<p>Manifest reminds you when there is no recovery file, and tells you how much
work is currently held on that handset alone.</p>
""",
            },
            {
                "id": "removing",
                "heading": "Removing a handset",
                "body": """
<p>Removing a paired handset frees a slot. It is worth being exact about what it
does and does not do, and the app says so on the screen rather than leaving you
to find out:</p>

<div class="warn"><p><strong>Removing revokes nothing.</strong> That handset
keeps the fleet key it already has and goes on opening every catalogue it
already holds, for ever. There is no way to reach it and no server to tell it
otherwise. What removal does is take it off the list, so nothing you seal
<em>from now on</em> can be opened by it.</p></div>

<p>If a handset is genuinely lost or in the wrong hands, <strong>take it off
the list</strong>. That is the step that matters: a sealed export names the
handsets paired at the moment it is written, so the missing device is not a
recipient of anything you seal afterwards.</p>

<p><strong>Remove and re-key</strong> mints a new fleet key and writes a file
wrapping it for the handsets you keep. Be clear about what that does today:
<em>no handset can load such a file yet</em>, so on its own a re-key shuts
nothing out — keep the file with your backups against the day it can. Removal
from the list is what changes who can open what.</p>

<p>And nothing stops what is already on that phone being read. Once a file is on
a device you cannot reach, no app can reach back — one claiming otherwise would
be lying to you.</p>
""",
            },
            {
                "id": "transfer",
                "heading": "Copying settings to another device",
                "body": """
<p>Destination and source settings can be copied from one device to another —
useful when a second person needs the same job delivery set up, or when a Studio
is being replaced.</p>

<p><strong>Credentials do not travel.</strong> The transfer carries the shape of
each destination and leaves its passwords and tokens behind, and the receiving
device lists plainly what still needs a credential entering. A configuration
file that quietly contained API keys would be the kind of convenience nobody
asked for.</p>
""",
            },
            {
                "id": "privacy",
                "heading": "What we can see",
                "body": """
<p>Nothing.</p>

<p>There is no Manifest account, no Manifest cloud and no Manifest server. We do
not receive your catalogue, your jobs, your photographs or your customers'
signatures — not because we promise not to look, but because no such destination
exists.</p>

<ul>
<li>The database <strong>and the photographs</strong> on the handset are
encrypted at rest, with the key held in the phone's own secure hardware.</li>
<li>A catalogue that was not signed by your Studio, or was altered on its way,
is <strong>refused</strong> by a paired handset. Studio authors catalogues, so
its own imports are not held to a signature.</li>
<li>A plain export has stored credentials stripped out of it, so handing
somebody your catalogue does not hand them your API keys. The exception is a
secret written into a destination's address, which cannot be removed without
breaking the address — Studio warns you where you author one.</li>
<li>Studio will not run on a phone with no screen lock.</li>
</ul>

<p>The full detail, including what a job can contain when your form asks for a
name or a signature, is in the <a href="%POLICY%">privacy policy</a>.</p>
""",
            },
        ],
    },
    # ---------------------------------------------------------------- pricing
    {
        "slug": "pricing",
        "title": "Price and scope",
        "blurb": "What it costs, what each tier includes, and what the app deliberately does not do.",
        "sections": [
            {
                "id": "price",
                "heading": "One payment, no subscription",
                "body": """
<p>You buy it once and it keeps working — offline, in five years, and if we are
hit by a bus. There is no renewal, no seat count to true up and nothing that
stops working because a card expired.</p>

<p><strong>Every paid tier carries the full feature set.</strong> What changes
is how many handsets you can pair — and one other thing: the catalogue server
add-on can only be bought on Team or Fleet.</p>

<p>Play has no upgrade path for a one-time purchase, so moving from Solo to Team
later means paying for Team rather than the difference. Worth knowing before you
choose.</p>
"""
                + tier_table()
                + """
<p>The handset app is <strong>free</strong>. You pay once, for Studio, on the
single phone that authors the catalogue.</p>
""",
            },
            {
                "id": "addon",
                "heading": "The catalogue server add-on",
                "body": """
<p>The <a href="data.html#server">catalogue server</a> is bought separately and
needs Team or Fleet, because it exists so that many handsets can pull a
catalogue without somebody handing each one a file. At a single handset, the
file is less work than a listening socket.</p>

<p>It is a one-time purchase like everything else.</p>
""",
            },
            {
                "id": "not",
                "heading": "What it deliberately is not",
                "body": """
<p>Being straight about this saves everybody a wasted evaluation.</p>

<div class="scroll"><table>
<thead><tr><th scope="col">Not</th><th scope="col">Why</th></tr></thead>
<tbody>
<tr><th scope="row">Stock control</th><td>Quantities are commercially sensitive
and go stale the moment they leave the system that owns them</td></tr>
<tr><th scope="row">Scheduling or dispatch</th><td>Seeing the work assigned to
you and recording that it was done — yes. Planning who goes where next week —
no</td></tr>
<tr><th scope="row">A sync engine</th><td>Each device holds its own copy.
Nothing silently merges behind your back</td></tr>
<tr><th scope="row">Multi-user with accounts</th><td>There are no user accounts
to administer. A device is the unit of identity</td></tr>
<tr><th scope="row">An editor for everyone</th><td>Authoring is Studio's job, so
the catalogue survives contact with a busy Friday</td></tr>
</tbody></table></div>
""",
            },
        ],
    },
    # ---------------------------------------------------------------- answers
    {
        "slug": "questions",
        "title": "Questions",
        "blurb": "The things people reasonably want to know before installing anything.",
        "sections": [
            {
                "id": "trying",
                "heading": "Can I try it before paying?",
                "body": """
<p>Yes. The free tier is a complete Studio on one device — author a catalogue,
import your spreadsheet, design job forms, record jobs and preview a label
sheet. Four things are paid, and they are the ones that take your work off the
handset: <strong>pairing</strong> other handsets, <strong>writing a recovery
file</strong>, <strong>sealing</strong> an export, and <strong>saving a label
sheet as a PDF</strong>. Checking and restoring a recovery file are free on
every tier, always — the moment you need a backup is the moment you have
least.</p>

<p>So you can find out whether the app suits your business before spending
anything, and the thing you pay for is putting it in other people's hands.</p>
""",
            },
            {
                "id": "leaving",
                "heading": "What happens to my data if I stop using it?",
                "body": """
<p>You export it and keep it. A plain export is an ordinary readable document
that any tool can open — deliberately, because a format only our software can
read would be lock-in wearing a security badge.</p>

<p>Nothing expires. You bought it once; it keeps working offline whatever
happens to us.</p>
""",
            },
            {
                "id": "internet",
                "heading": "Does it need the internet at all?",
                "body": """
<p>Only for three things, all optional: buying a tier, fetching a catalogue
update from an address you configured, and sending completed jobs to a
destination you configured.</p>

<p>Everything else — the entire daily use of the app — happens on the handset.
A business that hands catalogues around as files and keeps its job sheets on the
phone never needs a connection at all.</p>
""",
            },
            {
                "id": "size",
                "heading": "How big can a catalogue be?",
                "body": """
<p>Catalogues of several thousand parts are ordinary, and browsing and search
are built to stay quick at that size rather than degrade politely. The practical
limit is the phone's storage, and photographs use far more of it than the parts
do.</p>
""",
            },
            {
                "id": "existing",
                "heading": "I already have my parts in a spreadsheet",
                "body": """
<p>Good — that is the expected starting point.
<a href="data.html#spreadsheet">Import it</a>, correct the column mapping, and
you have a catalogue. If the spreadsheet is a mess, use the
<a href="catalogue.html#ai">AI conversion schema</a>: send it and your file to
any AI assistant and it will produce something importable.</p>
""",
            },
            {
                "id": "accounts",
                "heading": "How do I manage users?",
                "body": """
<p>You do not, because there are none. A device is the unit of identity: you
pair a handset, and that handset can read your catalogues. There is no user
directory, no password resets and no leavers process beyond
<a href="safety.html#removing">removing the handset</a>.</p>

<p>Jobs can still record who did the work, as a field on the form, because that
is a fact about the job rather than a login.</p>
""",
            },
            {
                "id": "android",
                "heading": "Is there an iPhone version?",
                "body": """
<p>Not today. Manifest and Manifest Studio are Android applications.</p>
""",
            },
            {
                "id": "support",
                "heading": "Something is wrong, or I need a hand",
                "body": """
<p>Both apps carry a built-in guide, and Studio can report on the health of your
catalogue. For anything else, the contact address is in the
<a href="%POLICY%">privacy policy</a>.</p>
""",
            },
        ],
    },
    # -------------------------------------------------------------- reference
    {
        "slug": "reference",
        "title": "Reference",
        "blurb": "Every field type, and the words this guide uses.",
        "sections": [
            {
                "id": "types",
                "heading": "Field types",
                "body": """
<p>All 44 types a field can hold. Each knows what it is, so the app shows it and
sorts it correctly, and most have a control for entering one. Two have no editor
anywhere yet — <code>file</code> and <code>geoPoint</code>. <code>audio</code>
and <code>video</code> can be filled in on a job but not on a part, and
<code>signature</code> is a job field only. A catalogue that already carries any
of these still shows and sorts them.</p>
"""
                + field_type_table(),
            },
            {
                "id": "glossary",
                "heading": "Glossary",
                "body": """
<div class="spec">
  <div><p class="k">Catalogue</p><div class="v"><p>The document holding your
  fields, structure, appearance and parts. The thing the app takes its shape
  from.</p></div></div>
  <div><p class="k">Part</p><div class="v"><p>One record. Depending on your
  trade that is a stock line, a fitting, or one individually tracked
  asset.</p></div></div>
  <div><p class="k">Build</p><div class="v"><p>A group of parts treated as a
  unit. You can call it a Kit, an Assembly or whatever your trade
  says.</p></div></div>
  <div><p class="k">Plan</p><div class="v"><p>A site drawing with zones marked
  on it and parts placed in them.</p></div></div>
  <div><p class="k">Job</p><div class="v"><p>One piece of recorded work, filled
  in on a form you designed.</p></div></div>
  <div><p class="k">Destination</p><div class="v"><p>Somewhere a completed job
  is sent — a folder, a web address or an email address.</p></div></div>
  <div><p class="k">Studio</p><div class="v"><p>The authoring app. One per
  business, on the phone that owns the catalogue.</p></div></div>
  <div><p class="k">Handset</p><div class="v"><p>A phone running the reading app,
  paired to a Studio.</p></div></div>
  <div><p class="k">Pairing</p><div class="v"><p>The face-to-face step that makes
  a handset trust your Studio's catalogues.</p></div></div>
  <div><p class="k">Recovery file</p><div class="v"><p>The encrypted file that
  lets a replacement phone become your Studio.</p></div></div>
</div>
""",
            },
        ],
    },
]
