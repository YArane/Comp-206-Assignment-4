#!/usr/bin/perl
use Data::Dumper;
use strict;
use CGI ':standard';

my $file = '../databases/members.csv';

sub checkUsernameExistence {
  open(INFO, "<$file");
  my @lines = <INFO>;
  close(INFO);

  foreach my $line (@lines) {
    #print "$line";

    my @words = split(/\s+/, $line);

    if (@words[0] eq @_[0]) {
      return 1;
    } 
    
  }
  return 0;
}

sub writeNewUserToDB {
  open(my $fh, '+>>', $file);
  print $fh "\n@_[0] @_[1]";
  close $fh;
}

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
		writeNewUserToDB($userData{'username'}, $userData{'password'});
		print "\t\t<center><h3>REGISTRATION SUCCESSFUL</h3></center>\n\t\t<p>Congratulations! New user created with the following credentials:<br>\n\t\t\tName: $userData{'name'}<br>\n\t\t\tUsername: $userData{'username'}<br>\n\t\t\tPassword: $userData{'password'}<br>\n\t\t\tYou may now log in.</p>\n";

	}else{
		print "\t\t<center><h3>REGISTRATION UNSUCCESSFUL</h3></center>\n\t\t<p>Another user already exists with  username: $userData{'username'}<br>\n\t\t\tPlease select another!</p>\n"
	}
	
	# print end
	print "\t\t<p><a href="index.html"><i>Back to homepage?</i></a></p>\n\t</body>\n</html>";
}

main();

