Feature: List questions/post

  #User Story: As a user, I want to be able to post questions

  Scenario: As a user, I want to be able to navigate from the homepage to the new question form
	Given I am on the homepage
	When I click on the questions page link
	Then I should be on the questions page
	When I click on the add question link
	Then I should be on the new question page
	And I should see the title field
	And I should see the text field
	
Feature: Reply to the question/post

  #User Story: As a user, I want to be able to reply to questions

  Scenario: As a user, I want to be able to navigate from the home page to the reply question to form
	Given I am on the homepage
	When I click on the questions page link
	Then I should be on the questions page
	When I click on the question page
	Then I should be on the question page
	When I click on the reply link
	Then I should be on the new reply page
	And I should see the text field
	
Feature: Edit/delete the question/post

  #User Story: As a user, I want to be able to edit questions

  Scenario: As a user, I want to be able to navigate from the homepage to the edit question form 
    Given I am on the homepage
	When I click on the questions page link
	Then I should be on the questions page
	When I click on the edit question link
	Then I should be on the edit question page
	And I should be able to edit the question that was posted
    And I should be able to delete the question that was posted
	And I should see the text field to edit
	
Feature: View a question/post

  #User Story: As a user, I want to be able to view questions

  Scenario: As a user, I want to be able to navigate from the homepage to the question page
	Given I am on the homepage
	When I click on the questions page link
	Then I should be on the questions page
	When I click on the individual question link
	Then I should be on the question page
	And I should be able to view a question and its replies
	
Feature: Rate a question/post

  #User Story: As a user, I want to be able to rate questions

  Scenario: As a user, I want to be able to navigate from the homepage to the question form and be able to rate the question
    Given I am on the homepage
	When I click on the questions page link
	Then I should be on the questions page
	When I click on the rate question up arrow or down arrow link
	Then I should be on the rate the question section
	And I should be able to rate up arrow or rate down the question that was posted