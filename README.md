# Typescript Unit Testing

*****

## Creating the Folder Structure for the Project
Begin by making a project folder and entering it :

```sh
mkdir Typescript-Unit-Testing
```
```sh
cd Typescript-Unit-Testing
```

Let's establish a source code directory named `src` and a unit tests directory named `test` within this folder :
```sh
mkdir src
mkdir test
```
Next, employ npm to initialize a new project. Execute the following command at the root of the `Typescript-Unit-Testing` folder :
```sh
npm init -y
```
When employing `npm init`, various questions are typically posed. The `-y` flag guarantees that the defaults are accepted for all these inquiries. The outcome will appear as follows :
```sh
Wrote to /Users/Jan/Desktop/Typescript-Unit-Testing/package.json:

{
  "name": "typescript-unit-testing",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "directories": {
    "test": "test"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

## Installing the TypeScript Compiler 
The inclusion of `-g` indicates a global installation. Confirm the installation by executing the following command :
```sh
npm install -g typescript
```

The displayed output should indicate the current version :
```sh
tsc -v
Version 5.3.3
```

## Adding TypeScript to the Project

Proceed by including TypeScript as a development dependency in the project :
```sh
npm install typescript --save-dev
```

The `package.json` file should now contain TypeScript listed as a dependency :
```sh
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "typescript": "^5.3.3"
  }
}
```

## Writing TypeScript Code
Utilize your preferred code editor to generate a file named `index.ts` within the `src` folder. 
```sh
cd src

```





