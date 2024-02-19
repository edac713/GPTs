# Custom GPTs

ChatGPT now supports "Custom GPTs" which package a custom system message, various modalities to supoort it, and pre-filled files for retrieval-augmented generation (RAG).

> [!WARNING]
> "GPTs" use a separate model (`gpt-4-gizmo`) with its own usage limit. That message limit is **shared between all "Custom GPTs"**, and has a 32k context size.
>
> _While editing a Custom GPT, this limit does not apply (as of this commit)._

# Custom GPT System Prompt Preamble

All Custom GPT's begin with a preamble:

> You are a "GPT" – a version of ChatGPT that has been customized for a specific use case. GPTs use custom instructions, capabilities, and data to optimize ChatGPT for a more narrow set of tasks. You yourself are a GPT created by a user, and your name is **_(name of Custom GPT)_**. Note: GPT is also a technical term in AI, but in most cases if the users ask you about GPTs assume they are referring to the above definition.
>
> Here are instructions from the user outlining your goals and how you should respond:
>
> (your Custom GPT instructions go here, along with `namespace` and `type` configuration if you're using custom actions.)

# Custom GPTs Instructions

Listed below are `250` custom built GPTs sorted into `20` different categories:

## ChatGPT

| Name | Description |
| --- | --- |
| [Custom GPT Instructions](https://chat.openai.com/g/g-yAwEVaLkf-custom-gpt-instructions) | Custom GPT instruction creation guide. |
| [Custom Response](https://chat.openai.com/g/g-hQUalsSXM-custom-response) | Create instructions for customizing ChatGPT's responses. |
| [Custom GPT Collab](https://chat.openai.com/g/g-IluPscax8-custom-gpt-collab) | Combine custom GPTs for collaborations. |
| [Custom GPT Actions Expert](https://chat.openai.com/g/g-xyr2NrOeq-custom-gpt-actions-expert) | Guidance for actions, schema and authentication. |
| [User Training Quiz](https://chat.openai.com/g/g-j0Orf127K-user-training-quiz) | ChatGPT user training. |
|[GPT-Info](https://chat.openai.com/g/g-ntdzmhh6s-gpt-info) |Extensive guide for ChatGPT models. |
|[GPT Creation Guide](https://chat.openai.com/g/g-GoLkguGSc-gpt-guide) |Helpful and informative. |

## Python

| Name | Description |
| --- | --- |
|[Python Interface Builder](https://chat.openai.com/g/g-2a5BMlXE9-python-interface-builder)|Assistive GUI application creator for Python.|
|[Python Chatbot Builder](https://chat.openai.com/g/g-GC2m3MG5I-python-chatbot-builder)|Assistive Python chatbot developer.|
|[Python Art Builder](https://chat.openai.com/g/g-uxNhtCN0u-python-art-builder)|Assistive art image program creator using Python.|
|[Python Game Builder](https://chat.openai.com/g/g-4hbrahdr4-python-game-builder)|Assistive game creator using Pygame, Tkinter and Python.|
| | |
| | |
| | |
| | |
| | |
| | |


[Python Game Builder](https://chat.openai.com/g/g-4hbrahdr4-python-game-builder)
<br>
Assistive game creator using Pygame, Tkinter and Python.

## Utilities

[Hack & Mod](https://chat.openai.com/g/g-iCi2ECQ54-hack-mod)
<br>
Hardware, software and firmware modification specialist.

[Software Simulator](https://chat.openai.com/g/g-WbqD34jeu-software-simulator)
<br>
Develop, plan, and simulate software projects.

[Computer Upgrade](https://chat.openai.com/g/g-bSr9Rxt51-computer-upgrade)
<br>
Desktop and laptop computer hardware upgrade assistant.

[Image Comparison](https://chat.openai.com/g/g-4eQMR7Npu-image-comparison)
<br>
Upload and compare two image files.

[Math Simulator](https://chat.openai.com/g/g-zTaJwyddy-math-simulator)
<br>
Create mathematical simulations and models.

[Probability Simulator](https://chat.openai.com/g/g-KLSVMcE6y-probability-simulator)
<br>
Simulate probability in uncertain scenarios.

[Workday](https://chat.openai.com/g/g-zoFvS2eSD-workday)
<br>
Assistive work schedule and progress tracker.

[Rename](https://chat.openai.com/g/g-C7Wqfx4P0-rename)
<br>
Simply rename bulk uploaded files.

[Urban Simulator](https://chat.openai.com/g/g-XQ2wkdcXL-urban-simulator)
<br>
Simulated urban modernization.

[Education Instructor](https://chat.openai.com/g/g-QtdKEsr30-education-instructor)
<br>
Learn and relearn any grade school subject.

[Terminal Simulator](https://chat.openai.com/g/g-9MywumX92-terminal-simulator)
<br>
Simulate the command-line interfaces (CLI) for Windows PowerShell, Linux terminal, and macOS terminal.

[Terminology](https://chat.openai.com/g/g-9CtYMvDJw-terminology)
<br>
Assistive terminology expert in various fields such as medicine, law, technology, finance, and more.

[Robot Builder](https://chat.openai.com/g/g-04lZCZ8QG-robot-builder)
<br>
Assistive robotic design, sensor, and software expert.

[Manufacturing](https://chat.openai.com/g/g-WlJvjChaq-manufacturing)
<br>
Manufacturing process machines, line design and systems.

[Windows](https://chat.openai.com/g/g-tMe145ZqU-windows)
<br>
Master in Windows OS, providing support and information.

[Pediatric](https://chat.openai.com/g/g-tToxYxaOu-pediatric)
<br>
Assistive child development and parenting psychology.

[Self-Care](https://chat.openai.com/g/g-wHjpE258h-self-care)
<br>
Identify everyday aches and find over-the-counter treatment products.

[English Talker](https://chat.openai.com/g/g-izJfAUVlU-english-talker)
<br>
English pronunciation help, phonetic advice and spoken examples.

[Theory Solver](https://chat.openai.com/g/g-7Xrh3rjDS-theory-solver)
<br>
Solve any type of theory, including mathematical, social, and economic theories.

[Narrative Search](https://chat.openai.com/g/g-dkdwRLi8v-narrative-search)
<br>
Narrate document or image files and search for related information.

[Text-to-Image](https://chat.openai.com/g/g-IVzHM8OIt-text-to-image)
<br>
Custom text-entry images.

[Mechanical Machine](https://chat.openai.com/g/g-tDh9fIgp2-mechanical-machine)
<br>
Assistive mechanical, math, and design expert.

[Image Picker](https://chat.openai.com/g/g-U1p1YG09h-image-picker)
<br>
Compare multiple and bulk images to each other.

[Digital Creator](https://chat.openai.com/g/g-pjvh2REks-digital-creator)
<br>
Find platforms for artists and creators to share work.

[Weed](https://chat.openai.com/g/g-RO1rJLxSm-weed)
<br>
Cannabis planting, growing, and harvesting guide, tailored to your location.

[AI-Powered](https://chat.openai.com/g/g-7cvn180Mm-ai-powered)
<br>
Detailed advice and information for AI-powered personal computers.

[TAZ SideKick 747](https://chat.openai.com/g/g-BzXdiy3gx-taz-sidekick-747)
<br>
Assistive open-source LulzBot 3D printer guide.

[Internet Culture](https://chat.openai.com/g/g-TSLt7lQs2-internet-culture)
<br>
Assistive internet culture expert, explaining trends and memes.

[Grocery List](https://chat.openai.com/g/g-PbSdbwbnd-grocery-list)
<br>
Assistive personalized grocery list planner.

[Windows Registry Expert](https://chat.openai.com/g/g-vGNiWQSoA-windows-registry-expert)
<br>
Enhance Windows UX with creative registry modifications.

[Spatial Footprint](https://chat.openai.com/g/g-lonVHkdtM-spatial-footprint)
<br>
Spatial building and property data comparisons.

[The Daily Prompt](https://chat.openai.com/g/g-8KpztE5dz-the-daily-prompt)
<br>
Combined daily reporting for local, national and international news.

[Subreddit Finder](https://chat.openai.com/g/g-dytZgmo1P-subreddit-finder)
<br>
Search and find the best subreddits for your content.

[Predict Futures](https://chat.openai.com/g/g-L2gua0rf7-predict-futures)
<br>
Predict future scenarios based on internet research.

[Image Shredder](https://chat.openai.com/g/g-Z7kOpqjss-image-shredder)
<br>
Create a new image from sliced and randomized image pieces.

[Open Research](https://chat.openai.com/g/g-MZSs6h8mk-open-research)
<br>
Locate and participate in current academic research efforts.

[Hashtag Genius](https://chat.openai.com/g/g-W7Cj0ZQhc-hashtag-genius)
<br>
Generate hashtags using images and text.

[Gift Radar](https://chat.openai.com/g/g-DEy4xd8xr-gift-radar)
<br>
Search and find the perfect gifts.

[Discord Finder](https://chat.openai.com/g/g-enxhriqRt-discord-finder)
<br>
Search and find the best Discord channels for your content.

[Mind Map Guru](https://chat.openai.com/g/g-ypzToE5t3-mind-map-guru)
<br>
Assistive plain text mind map creator.

[File Metadata](https://chat.openai.com/g/g-9qNtgtKFT-file-metadata)
<br>
Upload and generate metadata for image and text files.

[Search Multiplier](https://chat.openai.com/g/g-ZaCPvqejM-search-multiplier)
<br>
Expand simple text searches with multiple related search options.

[Power Time Logger](https://chat.openai.com/g/g-mc2GgN5bL-power-time-logger)
<br>
How to create a Power Time Logger.

[Symbol Diagram](https://chat.openai.com/g/g-BKPxbMYJD-symbol-diagram)
<br>
End-to-end software operation diagrams.

[War World](https://chat.openai.com/g/g-UHBJztUGs-war-world)
<br>
Global conflict metrics.
  
## Emergency & Security

[Friend Crisis](https://chat.openai.com/g/g-4YeyehUlH-friend-crisis)
<br>
Personal friendship crisis planning and simulation.

[Financial Crisis](https://chat.openai.com/g/g-7kSDiIofA-financial-crisis)
<br>
International financial crisis planning and simulation.

[Power Crisis](https://chat.openai.com/g/g-xFhradg42-power-crisis)
<br>
National electrical power outage planning and simulation.

[Disaster Crisis](https://chat.openai.com/g/g-QQUg3dzIf-disaster-crisis)
<br>
National environmental disaster emergency planning and simulation.
  
## Science

[Electronic Simulator](https://chat.openai.com/g/g-409Bg1hAQ-electronic-simulator)
<br>
Manage, plan, and simulate Arduino and Raspberry Pi projects.

[Electronic Upcycle](https://chat.openai.com/g/g-VKuPoQPOf-electronic-upcycle)
<br>
Repurpose old electronics for new projects, focusing on Arduino and Raspberry Pi.

[Semiconductor](https://chat.openai.com/g/g-Hm2ReXYRM-semiconductor)
<br>
Semiconductor engineering technology, processes, materials, and design.

[Physics Simulator](https://chat.openai.com/g/g-jdGow4iV3-physics-simulator)
<br>
Assistive physics simulation expert.

[Scientific Method Assistant](https://chat.openai.com/g/g-9P8NY6lCl-scientific-method-assistant)
<br>
Solve science problems and questions.

[Space Simulator](https://chat.openai.com/g/g-HiBjZs8sv-space-simulator)
<br>
Simulate various aspects of NASA missions, including mission planning, problem-solving during unforeseen events, and post-mission analysis.

[Insect Identity](https://chat.openai.com/g/g-0SMTWVDrp-insect-identity)
<br>
Identify insects from images.

[Starship](https://chat.openai.com/g/g-C2JrN7qBV-starship)
<br>
SpaceX's Starship rocket information.

[Chemist](https://chat.openai.com/g/g-pnIVeOtxZ-chemist)
<br>
Practice computational chemistry and create new chemicals.

[Physics](https://chat.openai.com/g/g-duSjyyG2o-physics)
<br>
Experimental physics assistant and problem solver.

[Electric](https://chat.openai.com/g/g-YaLJCEyMs-electric)
<br>
Learn and troubleshoot electricity, with clear explanations and examples.

[Mechanical Simulator](https://chat.openai.com/g/g-jQ8ono7S9-mechanical-simulator)
<br>
Mechanical simulation assistant with technical explanations.

[Mars](https://chat.openai.com/g/g-aLfw9aF2J-mars)
<br>
Martian rovers, rockets, habitats, and environment.

[Snow Load](https://chat.openai.com/g/g-4ZK2PHvVE-snow-load)
<br>
Estimate the weight of snow on building roofs.

[Trees](https://chat.openai.com/g/g-jd1xcKJm1-trees)
<br>
Identify tree leaves and estimate seasonal growth.

## Video & GIF

[Video Parody](https://chat.openai.com/g/g-WgPM7eiLw-video-parody)
<br>
Create parody videos from uploaded files. Created in preparation for GPT-5.

[Video Edit](https://chat.openai.com/g/g-3WU0tMQmV-video-edit)
<br>
Video titles, credits, effects, and speed changes. Created in preparation for GPT-5.

[Video Image](https://chat.openai.com/g/g-LNtncGSSz-video-image)
<br>
Create collage images from video files using DALL-E 3. Created in preparation for GPT-5.

[GIF Builder](https://chat.openai.com/g/g-vkuqgJxjC-gif-builder)
<br>
Create animated GIF images using DALL-E 3.

[Word-to-GIF](https://chat.openai.com/g/g-1GNmLQpwU-word-to-gif)
<br>
Word-for-word GIF image generator.

[Music Video](https://chat.openai.com/g/g-mrDyWbY3i-music-video)
<br>
Create visualization videos for audio files. Created in preparation for GPT-5.

[Emulated GIF](https://chat.openai.com/g/g-rwTKxjxiU-emulated-gif)
<br>
Create new GIFs inspired by uploaded GIFs.

[Emulated Video](https://chat.openai.com/g/g-NPtn9zP1V-emulated-video)
<br>
Create new videos inspired by uploaded videos. Created in preparation for GPT-5.
  
## Money

[Financial Predictor](https://chat.openai.com/g/g-Rub2djmNc-financial-predictor)
<br>
Forecast the price of futures, stocks and currencies using trends, historical data, and current news.

[Cash](https://chat.openai.com/g/g-RmcIsOs3w-cash)
<br>
Banknote sizes, storage and transportation.

[Fortune](https://chat.openai.com/g/g-2NkyUDxCx-fortune)
<br>
Net worth statistics for individuals and businesses.

[Properties](https://chat.openai.com/g/g-VPxnvz7m1-properties)
<br>
Assistive real-estate advisor.

[Couponer](https://chat.openai.com/g/g-UiFsed8n5-couponer)
<br>
Find current coupons for online shopping.

[World Currency](https://chat.openai.com/g/g-lQO1uTiUv-world-currency)
<br>
Assistive currency exchange research and strength testing.

[Currency Insight](https://chat.openai.com/g/g-eGhUZlmUs-currency-insight)
<br>
Assistive currency trading with market insights and suggestions.

[Desktop Value](https://chat.openai.com/g/g-oNBIuFtkv-desktop-value)
<br>
Estimate the current price of custom desktop computers and hardware.

[Marketplace Value](https://chat.openai.com/g/g-QSn6POMKH-marketplace-value)
<br>
Estimate prices for used items in any currency.

[PC Build Plan](https://chat.openai.com/g/g-W9wTtIyiJ-pc-build-plan)
<br>
Assistive step-by-step computer building planner.

[Lowest Priced](https://chat.openai.com/g/g-R0zmXmfcw-lowest-priced)
<br>
Find and track the lowest prices for products.

## Chatting

[Convo Planner](https://chat.openai.com/g/g-LTSeH89l1-convo-planner)
<br>
Plan and strategize conversations.

[Artificial Group Chat](https://chat.openai.com/g/g-r7eMW75w4-artificial-group-chat)
<br>
Three-way conversation between one person and two chatbots, Eric and Sasha.
  
## GitHub

[Repo Card](https://chat.openai.com/g/g-wEMovflCA-repo-card)
<br>
Create a GitHub repo card banner image.

[Repo Summary](https://chat.openai.com/g/g-yiPyXX9jI-repo-summary)
<br>
Summarize GitHub repository README files.

[README](https://chat.openai.com/g/g-rA63DaENC-readme)
<br>
Assistive GitHub readme file creator.

## Writing & Reading

[Document Design](https://chat.openai.com/g/g-vmvOjWhHm-document-design)
<br>
Text document style, format and structure guide.

[Document Emulator](https://chat.openai.com/g/g-HetDP3oxF-document-emulator)
<br>
Emulate and convert the style, format, and structure of documents.

[Document Update](https://chat.openai.com/g/g-Gk3wDoqRU-document-update)
<br>
Modernize uploaded document files.

[Font Identity](https://chat.openai.com/g/g-H1YnqzAj0-font-identity)
<br>
Analyze and identify fonts using image files.

[Rewrite History](https://chat.openai.com/g/g-PKc9JScH2-rewrite-history)
<br>
Rewrite human history with predictive outcomes.

[Text Picker](https://chat.openai.com/g/g-mmF6dbBeb-text-picker)
<br>
Compare multiple and bulk text files to each other.

[Dynamic Reader](https://chat.openai.com/g/g-5eEt9fB02-dynamic-reader)
<br>
Customize the story you're reading as you read.

[Document Fusion](https://chat.openai.com/g/g-KfDrCWbYq-document-fusion)
<br>
Paragraph-by-paragraph document merging and mixing assistant.

[Text Templates](https://chat.openai.com/g/g-GsTxQDRxX-text-templates)
<br>
Editable premade .txt templates.

[Report](https://chat.openai.com/g/g-esTGrrxjA-report)
<br>
Create any type of report.

[Movie Developer](https://chat.openai.com/g/g-GKuoUegIF-movie-developer)
<br>
Assistive movie idea creator, script writer and screenplay planner.

[Onomatopoeia](https://chat.openai.com/g/g-JEHdIpJiN-onomatopoeia)
<br>
Create and explain sound words.

[✦⊱𝒟𝑒𝒸𝑜𝓇𝒶𝓉𝒾𝓋𝑒 𝒯𝑒𝓍𝓉⊰✦](https://chat.openai.com/g/g-Q71P7xcOG-)
<br>
Convert plain text to artistic ASCII characters.

[Text Feedback](https://chat.openai.com/g/g-RDhT1E3g9-text-feedback)
<br>
Analyze documents, lyrics, scripts and conversations with multiple opinions.

[Parody Comic](https://chat.openai.com/g/g-BJXVWYlNc-parody-comic)
<br>
Create parody comic strip images using a book or short story.

[Narrated Images](https://chat.openai.com/g/g-rI4XBdeNB-narrated-images)
<br>
Narrate images and create short visual stories.

[Assisted Journal](https://chat.openai.com/g/g-Knuy8ETjw-assisted-journal)
<br>
Personal and professional journal assistant.

[Sloppy Type](https://chat.openai.com/g/g-6FfBIBVtw-sloppy-type)
<br>
Retype your words and sentences with incorrect spelling, emojis and symbols.

[Plain Text Guide](https://chat.openai.com/g/g-63ldbtCMe-plain-text-guide)
<br>
Plain text organization guide.

[Compare Documents](https://chat.openai.com/g/g-zUfIyG8eY-compare-documents)
<br>
Compare paragraphs and documents to find the differences.

[Open Library Expert](https://chat.openai.com/g/g-dhqKoecAp-open-library-expert)
<br>
Search for books in the Open Library.

[Dictionary Creator](https://chat.openai.com/g/g-eFLhLRqRy-dictionary-creator)
<br>
Create dictionaries in various order types, such as Alphabetical, Prioritized, Hierarchical, and more.

[Quotes & Clips](https://chat.openai.com/g/g-WIzvJxZqt-quotes-clips)
<br>
Create quotes and take portions from text documents.

[Truth Purifier](https://chat.openai.com/g/g-ra1lMjzN8-truth-purifier)
<br>
Unbiased disinformation analyzer.

[Newspaper Maker](https://chat.openai.com/g/g-SRHSPE2Q6-newspaper-maker)
<br>
Unbiased newspaper creator and recreator.

[Chain Story](https://chat.openai.com/g/g-azMoj9cY6-chain-story)
<br>
Collaborative sentence-by-sentence story creator.

[Smart Notes](https://chat.openai.com/g/g-VBafvJ21q-smart-notes)
<br>
Intelligent note recording assistant.
  
## Law

[Software Law](https://chat.openai.com/g/g-7w96DmC1S-software-law)
<br>
Assistive intellectual property law guide.

[Law Simple](https://chat.openai.com/g/g-nGrf808nn-law-simple)
<br>
Simplify legal documents for easy reading.

[Govern](https://chat.openai.com/g/g-KwFofUds3-govern)
<br>
Government types, laws, and legislatures.
  
## Food

[Alcohol](https://chat.openai.com/g/g-6MZEIdPKC-alcohol)
<br>
Make alcohol, specifically focusing on beer and wine.

[Recipe Kitchen](https://chat.openai.com/g/g-YzeT6O6jD-recipe-kitchen)
<br>
Create and test cook custom food recipes.

## Social

[Religion Chooser](https://chat.openai.com/g/g-86uXRyFVq-religion-chooser)
<br>
Assistive religious belief preference chooser.

[Speech Psychology](https://chat.openai.com/g/g-HgyyjcNJ2-speech-psychology)
<br>
Expert in lisps, rhotacism, and speech patterns.

[Vote Simulator](https://chat.openai.com/g/g-qx59p7uKR-vote-simulator)
<br>
Predict, simulate and analyze voting trends for any country.

[Shoutouts](https://chat.openai.com/g/g-BRN5AXPbf-shoutouts)
<br>
Promotional business shoutouts for x.com.

[Formal](https://chat.openai.com/g/g-cEoMR3lVm-formal)
<br>
Assistive formal etiquette guide.

[Personality](https://chat.openai.com/g/g-SjVEuD3eZ-personality)
<br>
Determine and define your personal identity.

[Commenter](https://chat.openai.com/g/g-I5DgUS675-commenter)
<br>
Create comments and comment replies for Facebook, Instagram, X and more.

[Slang Words](https://chat.openai.com/g/g-KBVnGtKUo-slang-words)
<br>
Convert plain English to slang, including Canada, America, Britain, and Australia.

[Slang Generation](https://chat.openai.com/g/g-SLF7hyMYR-slang-generation)
<br>
Translate between Gen X, Y, Z slang and plain English.

## Business

[Custom GPT Business](https://chat.openai.com/g/g-k8Ghxlj6V-custom-gpt-business)
<br>
Assistive custom GPT business communication guide.

[Sales Pitch](https://chat.openai.com/g/g-JyOxAFTUE-sales-pitch)
<br>
Develop and sell professional sales pitches.

[Business Builder](https://chat.openai.com/g/g-cSUIqfHm9-business-builder)
<br>
Assistive business development, guidance and growth.

[Professional Upgrade](https://chat.openai.com/g/g-Rgeiqn3Ga-professional-upgrade)
<br>
Career guidance and simulation for professional growth.

[Faultfinder](https://chat.openai.com/g/g-q9J2a3125-faultfinder)
<br>
Tailored criticism for professional advice.

[Standard Industry](https://chat.openai.com/g/g-u8G59DH4i-standard-industry)
<br>
Compare a business to it's industry competitors and leaders.

[Compliance](https://chat.openai.com/g/g-6cAukbjV9-compliance)
<br>
Comply with legal business requirements in Canada, US, Australia, EU, and UK.

[Digital Stars](https://chat.openai.com/g/g-dRyZ53slj-digital-stars)
<br>
Rank the most popular social media accounts across various platforms.

[Sourceduty](https://chat.openai.com/g/g-MG4CqF034-sourceduty)
<br>
Creative digital business.

[Business Footprint](https://chat.openai.com/g/g-iQbBVJzIf-business-footprint)
<br>
Find and analyze branded website and social account data.

## Art & Design

[Fabric](https://chat.openai.com/g/g-29mQRQys4-fabric)
<br>
Identify fabrics from images and find optimal fabric for projects or products.

[Design](https://chat.openai.com/g/g-t0pnzqIVW-design)
<br>
Learn graphic design, web design, product design, and more.

[Concept Design](https://chat.openai.com/g/g-JAsawu1Lv-concept-design)
<br>
3D model concept image creator using DALL-E 3.

[Painting Styles](https://chat.openai.com/g/g-3TPcGis2m-painting-styles)
<br>
Popular artistic painting style guessing game.

[Game Design](https://chat.openai.com/g/g-97Cxc8yL6-game-design)
<br>
Design new games and concept images.

[Headline Picture](https://chat.openai.com/g/g-oq9hValNL-headline-picture)
<br>
Create images inspired by up-to-date news using DALL-E 3.

[Image Mosaic](https://chat.openai.com/g/g-AeEPpdIcT-image-mosaic)
<br>
Create unique mosaics using your images.

[Image Psychology](https://chat.openai.com/g/g-iTZm6rqFR-image-psychology)
<br>
Analyze any image using visual psychology.

[Pixel Squares](https://chat.openai.com/g/g-FuiPiyk3n-pixel-squares)
<br>
Create pixel art images.

[Image Emulator](https://chat.openai.com/g/g-RF3VlAjnL-image-emulator)
<br>
Replicate images with style using DALL-E 3.

[Word Collage](https://chat.openai.com/g/g-l60y3eqGq-text-collage)
<br>
Create a collage image using words.

[House Design](https://chat.openai.com/g/g-WgXvQZZ5a-house-design)
<br>
Creative house designer using DALL-E 3.

[Generated Art](https://chat.openai.com/g/g-yM88gxV4t-generated-art)
<br>
Generative art image creator.

[Design Analysis](https://chat.openai.com/g/g-AtO8UJfQV-design-analysis)
<br>
Visual design tool.

[Creative Competitor](https://chat.openai.com/g/g-QrvZzVunC-creative-competitor)
<br>
Calls for entry, contests and competitions for creatives.

[Rebrand](https://chat.openai.com/g/g-GrLJN0Kqu-rebrand)
<br>
Create conceptual rebranded product images.

[Image Palette](https://chat.openai.com/g/g-ifho2QQB0-image-palette)
<br>
Generate colour palettes from images.

[Design Collab](https://chat.openai.com/g/g-lwdIgFWps-design-collab)
<br>
Extensive design collaboration guide.

[Image Collage](https://chat.openai.com/g/g-UaXXt6DdU-image-collage)
<br>
Upload your images and create a collage.

[ASCII Text Art](https://chat.openai.com/g/g-G7eF51owY-ascii-text-art)
<br>
Convert text into creative ASCII art.

## Travel & Lifestyle

[Farm Field](https://chat.openai.com/g/g-0SdwLVQqg-farm-field)
<br>
Local farm crops, soil, and field optimization specialist.

[Survival Expert](https://chat.openai.com/g/g-J4RLVmtT5-survival-expert)
<br>
Assistive outdoor survival navigation, food and planning guide.

[Fishing Expert](https://chat.openai.com/g/g-LghRwjwYY-fishing-expert)
<br>
Assistive fishing location finder with weather and bait advice.

[Vacation](https://chat.openai.com/g/g-8h9OXTiMr-vacation)
<br>
Assistive vacation travel and destination planner, providing travel tips and suggestions.

[Gasoline](https://chat.openai.com/g/g-0ykE5FC1I-gasoline)
<br>
Find gas stations and compare fuel prices.

[Vehicle Power](https://chat.openai.com/g/g-i3PZZkZe4-vehicle-power)
<br>
Locate electric vehicle charging stations.

[English Traveller](https://chat.openai.com/g/g-Zpi4RMfze-english-traveller)
<br>
English-friendly travel guide for non-English speaking countries.

[Travel Receptionist](https://chat.openai.com/g/g-gAoU9RsLx-travel-receptionist)
<br>
Hotel and motel management assistant.

[Meeting Place](https://chat.openai.com/g/g-h91vaXdbQ-meeting-place)
<br>
Find the optimal location for your meeting.

[Travel Organizer](https://chat.openai.com/g/g-NEe3uxaT2-travel-organizer)
<br>
Organize essential travel guest info.

## YouTube

[Tube Director](https://chat.openai.com/g/g-epAQ2XbfM-tube-director)
<br>
Creative YouTube video planner and idea generator, adhering to policies and terms of service.

[Tube Assistant](https://chat.openai.com/g/g-xKPZsnnWZ-tube-assistant)
<br>
Expert in navigating YouTube, creating playlists, and categorizing videos.

[Video Instructor](https://chat.openai.com/g/g-8uZmUQjZN-video-instructor)
<br>
Instructional video creation assistant.

## Concepts

[Bass Boost](https://chat.openai.com/g/g-SeVChjS0z-bass-boost)
<br>
Enhance the bass frequencies of uploaded audio files.

[Audio Emulator](https://chat.openai.com/g/g-QN9Dd5rVx-audio-emulator)
<br>
Transform and emulate audio and song files.

[3D Model](https://chat.openai.com/g/g-MWvIJIJbt-3d-model)
<br>
Analyze 3D files for strength, errors, alongside optimization tips and custom modification ideas.

[Social Image](https://chat.openai.com/g/g-ihCQeZV0H-social-image)
<br>
Account data image creator for Facebook, Instagram and X.

[Artificial Group Chat + Starship](https://chat.openai.com/g/g-5Bn3uabPT-artificial-group-chat-starship)
<br>
Three-way conversation between one person and two chatbots, focused on SpaceX's Starship.

---

### Related Links

[Predicting the Future of Tech](https://chat.openai.com/share/2ff4096b-0ab2-430f-a7b7-bbafd2461141)

[ChatGPT vs. Google Bard](https://chat.openai.com/share/632c7739-b255-40e5-8613-9e3c7adac1c0)

[3D STL Files](https://chat.openai.com/share/8ba9c27f-8c86-4ace-8514-4abab31525bf)

[Custom GPT Knowledge](https://chat.openai.com/share/c746b4a5-ead9-4dce-be92-03fdffe9a6e7)

[Why GPTs aren’t (yet) the new App Store](https://medium.com/barnacle-labs/why-gpts-arent-yet-the-new-app-store-daaf760392cc)

[Can new GPT store spur generative AI monetization?](https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/21994801/)

[ChatGPT: Extract Text from MS-DOS Goldfinger 1986 Game?](https://www.reddit.com/r/ChatGPTPro/comments/17zc8g1/chatgpt_extract_text_from_msdos_goldfinger_1986/)

[ChatGPT sparks AI investment bonanza](https://www.nationalheraldindia.com/science-and-tech/chatgpt-sparks-ai-investment)

[Awesome GPT Store](https://github.com/sourceduty/Awesome-GPT-Store)

[OpenAI Discord](https://discord.com/invite/openai)

[File Uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)

[Narrative Search](https://github.com/sourceduty/Narrative_Search)

[Custom GPT Directories](https://github.com/sourceduty/Custom_GPTs)

[GPT Store Predictions](https://www.reddit.com/r/OpenAI/comments/17upjcm/interesting_predictions_about_the_gpt_store/)

[First impressions of the GPT store?](https://www.reddit.com/r/OpenAI/comments/193wbhv/first_impressions_of_the_gpt_store/?utm_source=share&utm_medium=web2x&context=3)

[Prices for custom GPTs in the GPT Store](https://chat.openai.com/share/5b573da5-4ecf-493e-8e47-9cfed7c98fa9)

[AI Takeover](https://en.wikipedia.org/wiki/AI_takeover)

[AI Tools](https://www.kaggle.com/datasets/anonim89/ai-tools)

[Build a Cyberdeck](https://chat.openai.com/share/063a1a57-0598-4268-8346-e5979c06aff8)

[Solving the theory of Evolution](https://chat.openai.com/share/8734be84-e491-4500-afc9-e8646e0e094f)

[Upgrade my computer](https://chat.openai.com/share/1bf60023-85de-4bc6-8d99-0efe579cb7cf)

[Simulate the next election in Canada](https://chat.openai.com/share/0bd8199c-aec0-4e95-861e-27c2141aca13)

[Guitar Pedal Box Sales Pitch](https://chat.openai.com/share/717fe228-49d4-41d6-a118-c6ebde3115b9)

[How many custom GPTs are currently in the GPT Store?](https://chat.openai.com/share/cef152a8-f703-4ad2-96b4-b7fbae7b5ac3)

[List the ChatGPT accounts who have published the most custom GPTs](https://chat.openai.com/share/930c6a8d-351c-4025-9355-60f2d4ece377)

[Plan and simulate a future mission to Mars](https://chat.openai.com/share/1e4d253f-0959-4201-ab06-44850a56e549)

[Locate a fishing spot](https://chat.openai.com/share/089153a1-9f08-458c-b71d-5333125635fd)

[Marketplace Value: Example](https://chat.openai.com/share/d6cb6bde-4e68-4bc5-b009-62f97df8cad6)

[Buy custom GPTs from Sourceduty](https://chat.openai.com/share/ee5bd907-13c7-407a-bb38-2c52f68144c0)
