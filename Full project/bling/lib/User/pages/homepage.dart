import 'package:flutter/material.dart';

class Homepage extends StatefulWidget {
  const Homepage({super.key});

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Column(
        children: [
          Expanded(
            // For Search and notification
            flex: 1,

            child: Padding(
              padding: EdgeInsets.all(10),
              child: Row(
                children: [
                  Expanded(
                    flex: 12,
                    child: Container(
                      color: Colors.green,
                    ),
                  ),
                  Expanded(
                    flex: 2,
                    child: Container(
                      color: Colors.greenAccent,
                    ),
                  ),
                ],
              ),
            ),
          ),
          Expanded(
              flex: 1,
              child: Container(
                color: Colors.blue,
              )),
          Expanded(
              flex: 1,
              child: Container(
                color: Colors.black,
              )),
          Expanded(
              flex: 2,
              child: Container(
                color: Colors.grey,
              )),
          Expanded(
              flex: 1,
              child: Container(
                color: Colors.red,
              )),
          Expanded(
              flex: 5,
              child: Container(
                color: Colors.yellow,
              )),
          Expanded(
              flex: 2,
              child: Container(
                color: Colors.purple,
              )),
        ],
      ),
    );
  }
}
