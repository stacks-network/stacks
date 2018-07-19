. # Using the Blockstack Browser

The Blockstack browser gives users the ability to explore and use the
decentralized applications (dapps). The decentralized applications are a new way
to interact with the internet. Dapps give users control of their data. Data
about them personally, name, birthdate, phone number and data about what they do
such as visiting a website or buying an item.

## Understand the Blockstack Browser

Through the Blockstack browser you can create an identity. An identity
represents you as you interact with others through Dapps.  The Blockstack
browser is itself, a smiple Dapp. It allows you to:

* create one or more identities
* send and receive bitcoin
* manage the storage of your profile and application data
* find and launch Dapps

There are two versions of the Blockstack Browser, a web edition and a local
edition. If all you want to do is create, manage, and fund an identity you can
s[imply use the web edition](https://browser.blockstack.org/). If you want to
interact with Dapps built with the Blockstack platform or develop a Dapp
yourself, you need to download and install the browser's local edition.

## Install the local Browser

The installers are available from [the Blockstack website](https://blockstack.org/install).

## On Mac

1. Download the Mac installer.

## On Windows


## On Linux

The Blockstack installer on Linux requires Docker.  Before installing
Blockstack, install the version of Docker appropriate for your operating system.

**Note**: The Blockstack script used in the rest of this section involve running `docker` via the script. Depending on how you install and configure Docker on your system, it may or may not be necessary to have `root` or `sudo` privileges.  For this reason, the commands below show the use of `sudo` when interacting with the script or the `docker` executable.


1. Download [the installation script](https://github.com/blockstack/blockstack-browser/releases/download/v0.30.0/Blockstack-for-Linux-v0.30.0.sh).

   This downloads a `Blockstack-for-Linux-v0.30.0.sh` script to your local drive.

2. Open a terminal and navigate to the directory containing the downloaded script.

   When the script downloads, it is not executable.

3. Set the executable bit on the file.

    ```bash
    $ chmod u+x Blockstack-for-Linux-v0.309.0.0.sh
    ```
4. Use the script to `pull` the Blockstack Docker images you need.


    ```bash
    $ sudo ./Blockstack-for-Linux-v0.309.0.0.sh pull
    ```

    Depending on your network speed this can take some time.

5. Use the `docker image ls` command to confirm you have the image.
6.     **Note**: The commands in this sect





## Uninstall the browser

If you installed the browser using an installer, follow the instructions for
your operating system.

## On Mac

1. Use the Finder to open the **Applications** folder.
2. Locate the Blockstack application.
3. Drag the appliation to the trash.
4. Delete the `/Users/`_`YOURUSER`_`/Library/Application Support/Blockstack` folder.

   From the command line:

   ```bash
   $ rm -r /Users/moxiegirl/Library/Application\ Support/Blockstack
   ```

## On Windows




## On Linux




## Install a local Blockstack browser

You have Blockstack Browser installed: If you start from ADD USERNAME from IDs window, jump to 6.
1. You do not have the Blockstack Browser installed: go to https://explorer.blockstack.org/ 67
2. Search for your name typing “yourname.id” on the search box. If your .id is “free”, the response will be “Ooops ! The name yourname.id doesn’t exist.” or will show a owner “mnbhbu235j46ijnowejjybjb” with Expires field empty and just NAME_IMPORT, no NAME_REGISTRATION.
3. Install de Blockstack Browser, open an account, write by hand on a piece of paper and make two copies of mnemonic 12 words phrase, DO NOT KEEP IT IN THE COMPUTER, DO NOT UPLOAD IT TO THE CLOUD, DO NOT COPY IT IN THE CLIPBOARD.
4. Go to IDs
5. Click ADD USERNAME. (or MORE and CREATE NEW ID if you want more than one .id’s)
6. Try your selected name (without “.id”)
7. If available, check the price.
(If you want to buy a name with your wallet empty the process is a little more complex because the transfer can take a long time and the process will seems frozen, so I recommend to supply your wallet before, go to step 8)
8. Click WALLET
9. Fund your wallet with the correct amount or more.
10. Wait until you see the bitcoin amount in your wallet. Sometimes bitcoin net can take a minute or one hour (or 5) to perform the transaction depending on the demand of network operations, in the following link you will see approx. the time it will take to complete the transaction based on your fee: https://bitcoinfees.earn.com/ 18
10. Back to ADD USERNAME
11. Write your name and click search.
12. Click BUY
13. The process takes one hour or six blocks, DO NOT TURN OFF the browser or the computer for two hours.
