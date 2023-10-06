

class Legal:
    def __init__(self,type):
        self.type = type
        self.title = self.create_title()
        self.date = self.create_date()
        self.text = self.create_text()
    
    def create_title(self):
        if self.type == 'privacy-policy':
            title = 'Privacy Policy'
        elif self.type == 'cookies-policy':
            title = 'Cookies Policy'
        else: # terms-of-use
            title = 'Terms of Use'
        return title
    
    def create_date(self):
        if self.type == 'privacy-policy':
            date = 'October 07, 2023'
        elif self.type == 'cookies-policy':
            date = 'October 07, 2023'
        else: # terms-of-use
            date = 'October 07, 2023'
        return date
    
    def create_text(self):
        if self.type == 'privacy-policy':
            text = {
            'Information We Collect': [
                """We collect information that you provide directly to us. For example, we may collect your name, email address, 
                and other information when you register for an account or communicate with us.""",
                """We may also collect information about your use of our website and services, such as your IP address, browser 
                type, and operating system.""",
                """We may use cookies and similar tracking technologies to collect information about your interactions with our 
                website. You can manage your cookie preferences through your browser settings.""",
            ],
            'How We Use Your Information': [
                """We may use the information we collect for various purposes, including to provide and maintain our services, 
                improve our services, respond to your requests, and send you updates and marketing communications.""",
                """We may also share your information with third parties for purposes such as analytics, advertising, and other 
                business purposes.""",
            ],
            'Your Choices': [
                """You can access and update certain information you have provided to us by logging into your account and 
                adjusting your account settings.""",
                """You may also have certain rights under applicable data protection laws, including the right to access, 
                correct, or delete your personal information.""",
            ],
            'Security': [
                """We take reasonable measures to protect your personal information, but no data transmission over the internet 
                or information storage technology can be guaranteed to be 100% secure. We cannot ensure or warrant the security 
                of any information you transmit to us.""",
            ],
            'Changes to This Privacy Policy': [
                """We may update our Privacy Policy from time to time to reflect changes in our practices or for other 
                operational, legal, or regulatory reasons. We will notify you of any changes by posting the new Privacy Policy 
                on this page.""",
            ],
            'Contact Us': [
                """If you have any questions about this Privacy Policy or our practices, you can contact us at 
                info@replace.com.""",
            ]
            }
        elif self.type == 'cookies-policy':
            text = {
            "":["""This cookie policy ("Policy") describes what cookies are and how Website Operator ("Website Operator", 
            "we", "us" or "our") uses them on the mesural.com website and any of its products or services 
            (collectively, "Website" or "Services"). You should read this Policy so you can understand what type of
            cookies we use, the information we collect using cookies and how that information is used. It also describes
            the choices available to you regarding accepting or declining the use of cookies."""],
            "What are cookies?":["""Cookies are small pieces of data stored in text files that are saved on your computer
            or other devices when websites are loaded in a browser. They are widely used to remember you and your preferences,
            either for a single visit (through a "session cookie") or for multiple repeat visits (using a "persistent
            cookie"). Session cookies are temporary cookies that are used during the course of your visit to the Website,
            and they expire when you close the web browser. Persistent cookies are used to remember your preferences within
            our Website and remain on your desktop or mobile device even after you close your browser or restart your 
            computer. They ensure a consistent and efficient experience for you while visiting our Website or using our
            Services. Cookies may be set by the Website ("first-party cookies"), or by third parties, such as those who
            serve content or provide advertising or analytics services on the website ("third party cookies"). These third
            parties can recognize you when you visit our website and also when you visit certain other websites."""],
            "What type of cookies do we use?":["""Necessary cookies""","""Necessary cookies allow us to offer you the 
            best possible experience when accessing and navigating through our Website and using its features. For example,
            these cookies let us recognize that you have created an account and have logged into that account to access the
            content.""","""Functionality cookies""","""Functionality cookies let us operate the Website and our Services in
            accordance with the choices you make. For example, we will recognize your username and remember how you
            customized the Website and Services during future visits.""","""Analytical cookies""","""These cookies enable us
            and third-party services to collect aggregated data for statistical purposes on how our visitors use the Website.
            These cookies do not contain personal information such as names and email addresses and are used to help us
            improve your user experience of the Website."""],
            "What are your cookie options?":["""If you don't like the idea of cookies or certain types of cookies, you can
            change your browser's settings to delete cookies that have already been set and to not accept new cookies.
            To learn more about how to do this or to learn more about cookies, visit internetcookies.org. Please note,
            however, that if you delete cookies or do not accept them, you might not be able to use all of the features
            our Website and Services offer."""],
            "Changes and amendments":["""We reserve the right to modify this Policy relating to the Website or Services at
            any time, effective upon posting of an updated version of this Policy on the Website. When we do we will revise
            the updated date at the bottom of this page. Continued use of the Website after any such changes shall constitute
            your consent to such changes. Policy was created with WebsitePolicies."""],
            "Acceptance of this policy":["""You acknowledge that you have read this Policy and agree to all its terms and
            conditions. By using the Website or its Services you agree to be bound by this Policy. If you do not agree to
            abide by the terms of this Policy, you are not authorized to use or access the Website and its Services."""],
            "Contacting us":["""If you would like to contact us to understand more about this Policy or wish to contact us
            concerning any matter relating to our use of cookies, you may send an email to info@replace.com"""]
            }
        else: # terms-of-use
            text = {
            "Agreement to terms": ["""
            These Terms of Use constitute a legally binding agreement made between you, whether personally or on behalf of
            an entity (“you”) and Replace ("Company", “we”, “us”, or “our”), concerning your access to and use of the
            www.replaceup.com website as well as any other media form, media channel, mobile website or mobile application
            related, linked, or otherwise connected thereto (collectively, the “Site”). You agree that by accessing the Site,
            you have read, understood, and agreed to be bound by all of these Terms of Use. IF YOU DO NOT AGREE WITH ALL OF
            THESE TERMS OF USE, THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE SITE AND YOU MUST DISCONTINUE USE
            IMMEDIATELY.""",
            """Supplemental terms and conditions or documents that may be posted on the Site from time to time are hereby
            expressly incorporated herein by reference. We reserve the right, in our sole discretion, to make changes or 
            modifications to these Terms of Use at any time and for any reason. We will alert you about any changes by 
            updating the “Last updated” date of these Terms of Use, and you waive any right to receive specific notice of each
            such change. It is your responsibility to periodically review these Terms of Use to stay informed of updates. You 
            will be subject to, and will be deemed to have been made aware of and to have accepted, the changes in any revised
            Terms of Use by your continued use of the Site after the date such revised Terms of Use are posted.""",
            """The information provided on the Site is not intended for distribution to or use by any person or entity in any 
            jurisdiction or country where such distribution or use would be contrary to law or regulation or which would 
            subject us to any registration requirement within such jurisdiction or country. Accordingly, those persons who 
            choose to access the Site from other locations do so on their own initiative and are solely responsible for 
            compliance with local laws, if and to the extent local laws are applicable.""",
            """The Site is intended for users who are at least 18 years old. Persons under the age of 18 are not permitted to
            use or register for the Site.
            """],
            "Intellectual Property Rights": ["""
            Unless otherwise indicated, the Site is our proprietary property and all source code, databases, functionality,
            software, website designs, audio, video, text, photographs, and graphics on the Site (collectively, the “Content”)
            and the trademarks, service marks, and logos contained therein (the “Marks”) are owned or controlled by us or
            licensed to us, and are protected by copyright and trademark laws and various other intellectual property rights
            and unfair competition laws of the United States, international copyright laws, and international conventions.
            The Content and the Marks are provided on the Site “AS IS” for your information and personal use only. Except as
            expressly provided in these Terms of Use, no part of the Site and no Content or Marks may be copied, reproduced,
            aggregated, republished, uploaded, posted, publicly displayed, encoded, translated, transmitted, distributed, sold,
            licensed, or otherwise exploited for any commercial purpose whatsoever, without our express prior written permission.""",
            """Provided that you are eligible to use the Site, you are granted a limited license to access and use the Site and
            to download or print a copy of any portion of the Content to which you have properly gained access solely for your
            personal, non-commercial use. We reserve all rights not expressly granted to you in and to the Site, the Content
            and the Marks."""],
            "User representations": ["""
            By using the Site, you represent and warrant that: (1) all registration information you submit will be true, accurate,
            current, and complete; (2) you will maintain the accuracy of such information and promptly update such registration
            information as necessary; (3) you have the legal capacity and you agree to comply with these Terms of Use; (4) you
            are not a minor in the jurisdiction in which you reside; (5) you will not access the Site through automated or non-human
            means, whether through a bot, script, or otherwise; (6) you will not use the Site for any illegal or unauthorized purpose;
            and (7) your use of the Site will not violate any applicable law or regulation.""",
            """If you provide any information that is untrue, inaccurate, not current, or incomplete, we have the right to suspend or
            terminate your account and refuse any and all current or future use of the Site (or any portion thereof)."""],
            "Contact us": ["""
            In order to resolve a complaint regarding the Site or to receive further information regarding use of the Site, please
            contact us at:""",
            """Replace: Mallorca 319, Barcelona 08037 Spain info@replace.com"""]            
            }
        return text