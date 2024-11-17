import 'dart:convert';
import 'package:http/http.dart' as http;

// Access token for authentication
// Insert your access token here:
String accessToken = '';

// Function to get account ID
Future<String?> getAccountId() async {
  final url = Uri.parse('https://api.monzo.com/accounts');
  final headers = {
    'Authorization': 'Bearer $accessToken',
  };

  final response = await http.get(url, headers: headers);

  // Check if the request was successful
  if (response.statusCode == 200) {
    final accounts = jsonDecode(response.body)['accounts'];
    if (accounts.isNotEmpty) {
      return accounts[0]['id']; // Returns the first account's ID
    } else {
      print("No accounts found.");
      return null;
    }
  } else {
    print('Failed to get accounts. Status code: ${response.statusCode}');
    return null;
  }
}

// Function to get balance for the account
Future<void> getBalance(String accountId) async {
  final url = Uri.parse('https://api.monzo.com/balance?account_id=$accountId');
  final headers = {
    'Authorization': 'Bearer $accessToken',
  };

  final response = await http.get(url, headers: headers);

  // Check if the request was successful
  if (response.statusCode == 200) {
    final balance = jsonDecode(response.body);
    print('Balance: ${balance['balance']} GBP');
  } else {
    print('Failed to get balance. Status code: ${response.statusCode}');
  }
}

void main() async {
  final accountId = await getAccountId();
  if (accountId != null) {
    await getBalance(accountId);
  }
}
