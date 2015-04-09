#!/usr/bin/perl
use Data::Dumper;
use strict;
use CGI ':standard';

my $file = '../databases/members.csv';

# Validates that the specified username exists in the database
# Returns 1 if this is the case, and 0 if not.
sub checkUsernameExistence {
  open(INFO, "<$file");
  my @lines = <INFO>;
  close(INFO);

  foreach my $line (@lines) {
    #print "$line";

    my @words = split(/\s+/, $line);

    if (@words[1] eq @_[0]) {
      return 1;
    } 
    
  }
  return 0;
}

# Creates a new entry in the members DB.
# Stores the username, password, and name.
sub writeNewUserToDB {
  open(my $fh, '+>>', $file);
  print $fh "@_[0] @_[1] @_[2]\n";
  close $fh;
}

# Parses the query received so that the username/password/name values are stored in a hash
sub parseQuery{
	my @userData = split(/&/, @_[0]);
	my %FORM;
	foreach my $entry (@userData){
		(my $key, my $value) = split(/=/, $entry);
		$value =~ tr/+/ /;
		$value =~ s/%(..)/pack("C", hex($1))/eg;
		$FORM{$key} = $value; 
	}
		
	return %FORM;
}

# Registers the new user and prints the html explaining whether the operation was successful
# or not
sub main {
	#read query from post
	read(STDIN, my $query, $ENV{'CONTENT_LENGTH'});
	#parse query
	my %userData = parseQuery($query);

	# print start
	print "Content-type:text/html\r\n\r\n";
	print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>REGISTRATION STATUS</title>\n\t</head>\n\t<body>\n";

	#validate username
	if(checkUsernameExistence($userData{'username'}) == 0){
		writeNewUserToDB($userData{'name'}, $userData{'username'}, $userData{'password'});
		print "\t\t<center><h1>REGISTRATION SUCCESSFUL</h1></center>\n\t\t<p>Congratulations! New user created with the following credentials:<br><br>\n\t\t\t&emsp;Name: $userData{'name'}<br>\n\t\t\t&emsp;Username: $userData{'username'}<br>\n\t\t\t&emsp;Password: $userData{'password'}<br>\n\t\t\t<br>You may now log in.</p>\n";

	}else{
		print "\t\t<center><h1>REGISTRATION UNSUCCESSFUL</h1></center>\n\t\t<p>Another user already exists with username: $userData{'username'}<br>\n\t\t\tPlease select another.</p>\n"
	}
	
	# print end
	print "\t\t<p><a href=\"../index.html\"><i>Back to homepage?</i></a></p>\n\t</body>\n</html>";
}

main();