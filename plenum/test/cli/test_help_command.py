def testDefaultHelp(cli):
    """
    Testing `help` command
    """
    cli.enterCmd("help")
    defaultHelpMsg = """Plenum-CLI, a simple command-line interface for a
            Plenum protocol sandbox.
    Commands:
        help - Shows this help message
        help <command> - Shows the help message of <command>
        new - creates one or more new nodes or clients
        keyshare - manually starts key sharing of a node
        status - Shows general status of the sandbox
        status <node_name>|<client_name> - Shows specific status
        list - Shows the list of commands you can run
        license - Show the license
        exit - exit the command-line interface ('quit' also works)
        prompt <principal name> - Changes the prompt to <principal name>
        principals (a person like Alice, an organization like Faber College, or an IoT-style thing)
        load <invitation filename> - Creates the link, generates Identifier and signing keys
        show <invitation filename> - Shows the info about the link invitation
        show link <name> - Shows link info in case of one matching link, otherwise shows all the matching link <names>
        connect <test> |<live> - Let's you connect to the respective environment
        sync <link name> - Synchronizes the link between the endpoints"""

    msg = cli.lastPrintArgs['msg']
    assert msg == defaultHelpMsg


def testNew(cli):
    """
    Testing `help new` command
    """
    cli.enterCmd("help new")
    newMsg = """Is used to create a new node or a client.
                     Usage: new <node/client> <nodeName/clientName>"""
    msg = cli.lastPrintArgs['msg']
    assert msg == newMsg


def testNewNode(cli):
    """
    Testing `help new node` command
    """
    cli.enterCmd("help new node")
    newMsg = "It is used to create a new node"
    msg = cli.lastPrintArgs['msg']
    assert msg == newMsg


def testNewClient(cli):
    """
    Testing `help new client` command
    """
    cli.enterCmd("help new client")
    newMsg = "It is used to create a new client"
    msg = cli.lastPrintArgs['msg']
    assert msg == newMsg
