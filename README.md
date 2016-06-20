# rentspace

This document is main source for all technical and non technical things related to projects.

TOC
Documents
Requirements
Usecases
MOM
Issues
ActionItems
Others


==>Documents
docs/software.info -> for tools and technologies used in this project
docs/db_schema.info -> for database tables, fields
docs/rest_api.info -> for rest API exposed by this app
wireframes-mockups -> for wireframes of this web app
project_plan.info -> more details about development plan, screens, issues etc..
 
==>Requirements

==>Usecases
# No seperate login for clients/users

# Seperate login for admin people to maintain the website.
  Some screens are available only to admin people
    
# User1 is looking for accomdation and interested in property posted by user2
  option1: user2 doesn't post available dates of property
        user1 express interest in property
        the details are sent to user2
        user2 responds back to user1
    option2: user2 gives start date and end date
        between dates the ad is active.
        after the end date the ad becomes inactive
        don't show the property in search results

==>Issues

==>MOM
May 22
    Google cloud messaging services
    GCM registraion  (mobile users)
    Additional fields to add for users for android/ios

Jun 19th
   Providing calendar option to user to enter all the dates for availibility of accomdation
   # Option1
     Allow customer to specify accomdation dates for 45 days or 60 days etc
   
   Fixing the price of accomdation
   Discussion about whether to have payment gateway or not
    # Option1
      Release the app to public without payment gateway
      Initially provide the service for free of cost. 
      Collect the feedback and identity the real time issues.
      Fix the issues in process, enhance the webapp/android app with more features
      Integrate the app with payment gateway and start collecting the money
    # Option2
      Release beta version just to close friends, selected users
      Collect the feedback and identity the real time issues.
      Integrate the app with payment gateway and release to public
    # Option3
      Take enough time to discuss about process, development
      Release the webapp and android app with payment gateway
      
      
      


==>ActionItems
    -> Check about how to validate Aadhar card using the software provided by police dept or others
    -> Validating picture/location information provided by user
            verify pictures manually
            validate location using google map (similar to one in magicbricks or 99acres.)
            reference number. When someone is posting an ad for house, he can give reference number of apartment committe etc..
    -> safety and security
            provide contact details of service provider to poilce etc.
    -> Keep legal rules in Terms and conditions
    -> Check with advocate about terms and conditions

==>Others


-->Website names:
quickstay
estay
eroom
rentspace
oyebasera
eroost
ehoy/hoy








